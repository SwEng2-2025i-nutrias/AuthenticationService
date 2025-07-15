flowchart TB
    A["GET Request to /validate-token"] --> B["Auth Controller (Input Adapter): Get 'Authorization' header"]
    B --> C{"Header present?"}
    
    C -- No --> Z1["Return 401: Missing Authorization header"]
    Z1 --> End["End"]

    C -- Yes --> D{"Header starts with 'Bearer '"}
    D -- No --> Z2["Return 401: Invalid Authorization header format"]
    Z2 --> End

    D -- Yes --> E["Auth Controller: Extract token from header"]
    E --> F["Token Handler (Token Output Adapter): Verify token"]
    
    F --> G{"Token payload valid?"}
    G -- No --> Z3["Return 401: Invalid token payload"]
    Z3 --> End

    G -- Yes --> H["Extract email from payload"]
    H --> I{"Email present?"}
    I -- No --> Z4["Return 401: Invalid token payload"]
    Z4 --> End

    I -- Yes --> J["Auth Service (Input Port): Get user by email"]
    J --> K{"User found?"}
    K -- No --> Z5["Return 404: User not found"]
    Z5 --> End

    K -- Yes --> L["Return 200: Token is valid + user_id"]
    L --> End

    %% Color styles
    style A fill:#BBDEFB
    style B fill:#C8E6C9
    style C fill:#C8E6C9
    style Z1 fill:#C8E6C9
    style D fill:#C8E6C9
    style Z2 fill:#C8E6C9
    style E fill:#C8E6C9
    style F fill:#FFE0B2
    style G fill:#FFE0B2
    style Z3 fill:#C8E6C9
    style H fill:#C8E6C9
    style I fill:#C8E6C9
    style Z4 fill:#C8E6C9
    style J fill:#FFF9C4
    style K fill:#FFE0B2
    style Z5 fill:#C8E6C9
    style L fill:#C8E6C9
