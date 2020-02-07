from django.contrib import messages

import json

from .ssh import ssh_exec


def to_float(s):
    try:
        return float(s)
    except:
        return 0


class CommandError(Exception):
    pass


class Command:
    def __init__(self, request, action, *args):
        self.instance = request.security_user
        self.action = action
        if args:
            self.args = args

    def _run(self):
        err, out = ssh_exec(
            username=self.instance.group_identifier(),
            private_key_path=self.instance.private_key.path,
            command=self._command())

        if err:
            raise CommandError(out)
        return out

    def _command(self):
        if self.action == 'history':
            b"""       JobID      State    JobName                           User  Partition   NNodes      NCPUS     ReqMem                 End 
                ------------ ---------- ---------- ------------------------------ ---------- -------- ---------- ---------- ------------------- 
                14960            FAILED      a.out                 uclv_vmarreros     public        2         16     2746Mn 2019-12-13T10:05:52 
            """
            return 'sacct -S {date} -u {user} --format=jobid,state,jobname,user,partition,nnodes' \
                   ',ncpus,reqmem,end -X -P'.format(
                date=self.args[0],
                user=self.instance.group_identifier())
        if self.action == 'summary':
            b"""Job ID: 15000
                Cluster: mambi
                User/Group: uclv_efirvida/uclv
                State: COMPLETED (exit code 0)
                Nodes: 13
                Cores per node: 7
                CPU Utilized: 06:26:28
                CPU Efficiency: 62.33% of 10:20:00 core-walltime
                Memory Utilized: 1.33 GB
                Memory Efficiency: 3.81% of 34.86 GB
            """
            return 'seff {jobid}'.format(
                jobid=self.args[0])
        if self.action == 'jobs':
            return 'squeue -all --states=all -o "%i|%T|%j|%u|%P|%M|%l|%D|%R"'
        if self.action == 'job-detail':  # job id in parameters
            return 'scontrol show job -o {jobid}'.format(
                jobid=self.args[0])
        if self.action == 'job kill':  # Cancela el trabajo de la cola de ejecución.
            return 'scancel --signal=KILL {jobid}'.format(
                jobid=self.args[0])
        if self.action == 'job hold':  # Impide que se inicie una tarea pendiente (establece su prioridad en 0) si se esta ejecutando su prioridad se establece en 0 en caso de una nueva ejecución
            return 'scontrol hold {jobid}'.format(
                jobid=self.args[0])
        if self.action == 'job release':
            return 'scontrol release {}'.format(self.args[0])  # Libere un trabajo retenido anteriormente para comenzar la ejecución.
        if self.action == 'job suspend':
            return 'scontrol suspend {}'.format(self.args[0])  # Suspender un trabajo en ejecución. Si se pone en cola un trabajo suspendido, se colocará en estado retenido.
        if self.action == 'job resume':
            return 'scontrol resume {}'.format(self.args[0])  # Reanudar un trabajo previamente suspendido. Un trabajo suspendido libera sus CPU para su asignación a otros trabajos.
        if self.action == 'job requeue':
            return 'scontrol requeue {}'.format(self.args[0])  # Re-encolar un trabajo por lotes Slurm en ejecución, suspendido o terminado en estado pendiente.
        if self.action == 'job continue':
            return 'scancel --signal=CONT {}'.format(self.args[0])  # Reanuda la ejecución de un trabajo suspendido con sus recursos retenidos.
        if self.action == 'job stop':
            return 'scancel --signal=STOP {}'.format(self.args[0])  # Suspender un trabajo en ejecución y retiene los recursos asignados.

        # hpc script ########
        if self.action == 'partitions':
            return 'sinfo --format=%R'
        if self.action == 'execute':
            return 'sbatch "{}/{}"'.format(self.args[0], self.args[1])

        # hpc nodes ########
        if self.action == 'nodes':
            return 'scontrol show nodes -o'
        if self.action == 'nodes-partitions':
            return 'sinfo -N --Format=all'
        if self.action == 'cpusload':
            return 'sinfo -N --Format=nodelist,cpusload'
        if self.action == 'partitions-detail':
            return 'sinfo --format="%R %a %D %N"'

    def to_dict(self):
        str_bytes = self._run()
        str_utf8 = str_bytes.decode('utf-8').strip()

        __dict__ = dict()
        if self.action == 'nodes':
            nodes = list()
            cpu_load = cpu_total = cpu_alloc = free_mem = real_mem = 0
            for node in str_utf8.split('\n'):
                features = dict()
                for feature in node.split():
                    if len(feature.split('=')) == 2:
                        features.update({
                            feature.split('=')[0]: feature.split('=')[1]
                        })
                nodes.append(features)
                cpu_total = cpu_total + to_float(features['CPUTot'])
                cpu_alloc = cpu_alloc + to_float(features['CPUAlloc'])
                free_mem = free_mem + to_float(features['FreeMem'])
                real_mem = real_mem + to_float(features['RealMemory'])
            __dict__['nodes'] = nodes
            __dict__['summary'] = {
                'free_mem': free_mem,
                'real_mem': real_mem,
                'cpu_tot': cpu_total,
                'cpu_alloc': cpu_alloc}
        if self.action == 'partitions-detail':
            data = list()
            keys = str_utf8.split('\n')[0].split()
            for line in str_utf8.split('\n')[1:]:
                data.append(line.split())
            __dict__['partitions'] = {'data': data, 'keys': keys}
        if self.action == 'nodes-partitions':
            nodes = list()
            tmp = str_utf8.split('\n')
            keys = tmp[0].split('|')
            for node in tmp[1:]:
                nodes.append(node.split('|'))
            __dict__['keys'] = keys
            __dict__['nodes'] = nodes
        if self.action == 'cpusload':
            data = list()
            tmp = str_utf8.split('\n')
            keys = tmp[1].split()
            for node in tmp[1:]:
                data.append(node.split())
            __dict__['keys'] = keys
            __dict__['data'] = data
        if self.action == 'jobs':
            data = list()
            for line in str_utf8.split('\n')[2:]:
                data.append(line.split("|"))
            __dict__['data'] = data
        if self.action == 'job-detail':
            keys = [
                'JobId', 'JobName', 'UserId', 'GroupId', 'Priority', 'Account', 'QOS', 'JobState',
                'Reason', 'Requeue', 'Restarts', 'RunTime', 'TimeLimit', 'TimeMin', 'SubmitTime',
                'EligibleTime', 'StartTime', 'EndTime', 'Deadline', 'PreemptTime', 'SuspendTime',
                'SecsPreSuspend', 'Partition', 'AllocNode:Sid', 'ReqNodeList', 'NodeList', 'BatchHost',
                'NumNodes', 'NumCPUs', 'NumTasks', 'CPUs/Task', 'TRES', 'Command', 'WorkDir', 'StdErr',
                'StdIn', 'StdOut'
            ]
            fields = str_utf8.split()
            for key in keys:
                i = 0
                for field in fields:
                    if field.startswith(key):
                        if key == 'TRES':
                            __dict__['mem'] = field.split(',')[1].split('=')[1]
                        else:
                            __dict__[key] = field.split('=')[1]
                        break
                fields.pop(i)
            __dict__['Username'] = __dict__['UserId'].split('(')[0]
            __dict__['CPUsTask'] = __dict__.pop('CPUs/Task')
        if self.action == 'partitions':
            partitions = list()
            for partition in str_utf8.split('\n')[1:]:
                partitions.append(partition)
            __dict__['data'] = partitions
        if self.action == 'history':
            jobs = list()
            for line in str_utf8.split('\n')[1:]:
                jobs.append(line.split('|'))
            __dict__['data'] = jobs
        if self.action == 'summary':
            summary = dict()
            for line in str_utf8.split('\n'):
                summary[line.split(": ")[0]] = line.split(": ")[1]
            __dict__['summary'] = summary
        return __dict__

    def to_json(self):
        return json.dumps(self.to_dict())
