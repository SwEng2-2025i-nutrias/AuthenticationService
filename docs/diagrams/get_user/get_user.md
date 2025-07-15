flowchart TB
    A["GET Request to /users/<user_id>"] --> B["Auth Controller (Input Adapter): Extract user_id from URL"]
    B --> C["Auth Service (Input Port): Get user by ID"]
    C --> D{"User exists?"}
    
    D -- No --> Z1["Return 404: User not found"]
    Z1 --> End["End"]

    D -- Yes --> E["Return 200: Public user data as JSON"]
    E --> End

    D -- Exception --> Z2["Return 500: Internal Server Error (exception message)"]
    Z2 --> End

    %% Color styles
    style A fill:#BBDEFB
    style B fill:#C8E6C9
    style C fill:#FFF9C4
    style D fill:#FFE0B2
    style Z1 fill:#C8E6C9
    style E fill:#C8E6C9
    style Z2 fill:#C8E6C9
