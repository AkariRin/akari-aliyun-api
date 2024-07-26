from ..api import Api


class Ecs:
    def __init__(self, access_key_id, access_key_secret, host):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.host = host

    def reboot_instance(self, instance_id, force_stop, dry_run):
        request = Api(self.access_key_id, self.access_key_secret, "POST", self.host, "/",
                      "RebootInstance", "2014-05-26")
        request.param["InstanceId"] = instance_id
        request.param["ForceStop"] = force_stop
        request.param["DryRun"] = dry_run
        return request.exec()
