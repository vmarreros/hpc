from celery import shared_task

from .models import SoftwareInstalled, SoftwareVersion
from .ssh import ssh_exec
from src.application.security.models import LDAPUser


@shared_task()
def ___task___application___hpc___modules___synchronize___():
    command = 'module -t --redirect avail'
    instance = LDAPUser.objects.first()
    err, str_in_bytes = ssh_exec(username=instance.group_identifier(), private_key_path=instance.private_key.path, command=command)
    if err:
        return False
    string_in_utf8 = str_in_bytes.decode('utf-8').split('/opt/apps/easybuild/modules/all:\n')[1]\
        .replace('/opt/apps/manualy/modules/all:\n', '')
    modules = list()
    module = dict()
    pattern = "XXX"
    for line in string_in_utf8.split('\n'):
        if line.split("/")[0] == pattern:
            module["version"].append(line)
        else:
            if module:
                modules.append(module)
            module = {
                "name": line[:-1],
                "version": list()}
            pattern = line[:-1]

    for module in modules:
        obj, flag = SoftwareInstalled.objects.get_or_create(name=module["name"])
        if flag:
            obj.description = get_description(module["name"])
            obj.save()
        for version in module["version"]:
            SoftwareVersion.objects.get_or_create(version=version, software=obj)

    for obj in SoftwareInstalled.objects.all():
        exist = False
        for module in modules:
            if obj.name == module["name"]:
                exist = True
                break
        if not exist:
            obj.delete()
        else:
            exist = False
            for objv in obj.version_set.all():
                for version in module["version"]:
                    if objv.version == version:
                        exist = True
                        break
                if not exist:
                    objv.delete()
                else:
                    exist = False
    return True


def get_description(name):
    command = 'module -t --redirect whatis '
    instance = LDAPUser.objects.first()
    err, str_in_bytes = ssh_exec(username=instance.group_identifier(), private_key_path=instance.private_key.path, command=command + name)
    if err:
        return ''
    string_in_utf8 = str_in_bytes.decode('utf-8')
    return string_in_utf8.split('\n{}/'.format(name))[0].split('Description: ')[1].replace('\n', '')
