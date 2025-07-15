flowchart TB
    A["DELETE Request to /\_\_test__/database"] --> B["Auth Controller (Input Adapter): Check APP_ENV"]
    B --> C{"Is APP_ENV == 'test'?"}
    
    C -- No --> Z1["Return 403: Endpoint only available in test environment"]
    Z1 --> End["End"]

    C -- Yes --> D["Auth Service (Input Port): Delete user database"]
    D --> E["Return 200: Database deleted successfully"]
    E --> End

    D -- Exception --> Z2["Return 500: Internal Server Error (exception message)"]
    Z2 --> End

    %% Color styles
    style A fill:#BBDEFB
    style B fill:#C8E6C9
    style C fill:#C8E6C9
    style Z1 fill:#C8E6C9
    style D fill:#FFF9C4
    style E fill:#C8E6C9
    style Z2 fill:#C8E6C9