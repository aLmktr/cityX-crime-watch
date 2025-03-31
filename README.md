<div align="center">
   <img src="./data/citx-crime-watch-logo.png" alt="cityx-crime-watch-logo"/>
</div>
<br />

## 🚀 Getting Started

### Prerequisites

- Docker (if using the recommended setup)
- Python 3.12+

### 🔧 Installation

#### Clone the Repository

```bash
git clone https://github.com/aLmktr/cityX-crime-watch.git
cd cityX-crime-watch
```

<details open>
    <summary> 🐋 Build with Docker - Recommended </summary>

    1.  Run and build the docekr container

        ```bash
        docker compose up --build
        ```

</details>

<details>
    <summary>🗃️ Build it yourself</summary>
    
    1. Create a virtual environment:

       ```bash
       python -m venv venv
       source venv/bin/activate  # On Windows use `venv\Scripts\activate`
       ```

    2. Install dependencies:

       ```bash
       pip install -r requirements.txt
       ```

    3. Run the application:

       ```bash
       streamlit run src/app.py
       ```

</details>

## 🤝 Contributing

Contributions are welcome. Please fork the repo and submit a PR.

## 📄 License

This project is licensed under the MIT License.
