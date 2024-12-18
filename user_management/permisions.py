from rest_framework.permissions import BasePermission  

class IsFarmer(BasePermission):  
    def has_permission(self, request, view):  
        return request.user.user_type == 1  # Assuming 1 is Farmer  

class IsFarmAgent(BasePermission):  
    def has_permission(self, request, view):  
        return request.user.user_type == 2  # Assuming 2 is FarmAgent  

class IsVeterinaryPartner(BasePermission):  
    def has_permission(self, request, view):  
        return request.user.user_type == 3  # Assuming 3 is VeterinaryPartner  