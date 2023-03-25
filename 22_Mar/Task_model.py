class task:
    def __init__(self,id,taskname,description,priority):
        self.id=id
        self.taskname=taskname
        self.description=description
        self.priority=priority

    def __repr__(self):
        return f"Task id: {self.id},\ntask name: {self.taskname},\nDescription: {self.description},\nPriority: {self.priority}\n"

class taskStatus():
    def __init__(self,statuscode,message,taskobj):
        self.statuscode=statuscode
        self.message=message
        self.taskobj=taskobj

    def __repr__(self):
        return f"{self.statuscode},{self.message},{self.taskobj}"