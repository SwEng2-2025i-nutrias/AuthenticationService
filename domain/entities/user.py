class User:

    # Represents a user in the system.
    def __init__(self, id:str, email:str, password_hash:str, name:str, role:str, created_at:str, last_login_at:str|None=None):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.name = name
        self.role = role
        self.created_at = created_at
        self.last_login_at = last_login_at

    # Converts the User object to a dictionary representation.
    def to_dict(self) -> dict[str, str|None]:
        return {
            "id": self.id,
            "email": self.email,
            "password_hash": self.password_hash,
            "name": self.name,
            "role": self.role,
            "created_at": self.created_at,
            "last_login_at": self.last_login_at if self.last_login_at else None,
        }
    
    # Creates a User object from a dictionary representation.
    @classmethod
    def from_dict(cls, data: dict[str, str]):
        
        id = data["id"]
        email = data["email"]
        password_hash = data["password_hash"]
        name = data["name"]
        role = data["role"]
        created_at = data["created_at"]
        last_login_at = data.get("last_login_at", None)

        
        user = cls(id, email, password_hash, name, role, created_at, last_login_at)

        return  user
    
    def update_password(self, new_password_hash: str):
        """
        Updates the user's password hash.
        """
        self.password_hash = new_password_hash