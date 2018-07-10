import docker

class API():
    def __init__(self):
        self.host = docker.from_env()

    # return list of containers
    def list(self, verbose=False, all=False):
        api_containers = []
        if all:
            api_containers = self.host.containers.list(all=True)
        else:
            api_containers = self.host.containers.list(all=False)
            
        if verbose:
            containers = {}
            for i in api_containers:
                containers[i.name] = {'status': i.status, 'id': i.short_id}
            return containers
        else:
            return [ i.name for i in api_containers ]

    # docker host info
    def info(self):
        return self.host.info()

