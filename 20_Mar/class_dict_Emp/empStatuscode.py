
class EmployeeStatusCode():
    def __init__(self,statuscode,message,empobj):
        self.statuscode=statuscode
        self.message=message
        self.empobj=empobj

    def __repr__(self):
        return f"{self.statuscode},{self.message},{self.empobj}"








# class Rect:
#     def __init__(self,length,breadth):
#         print("hey how are you")
#  
#     def area(self):
#         return self.l*self.b
#    
#        
#     def __str__(self):
#         return 'junk'
#  
# class RectStatus:
#     def __init__(self,statuscode,statusmessage,rcto):
#         self.statuscode=statuscode
#         self.statusmessage=statusmessage
#         self.rectobj=rcto


#  
# #success scenario
# success=RectStatus(1,"got results successfully",Rect(2,3))
# rectobj=success.rectobj
# print(rectobj)

        