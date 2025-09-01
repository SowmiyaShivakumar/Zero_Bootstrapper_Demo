# Zero Bootstrapper Demo

## BMI Calculator Project

This project includes a simple BMI calculator implemented in React. It also features a FastAPI backend with an endpoint for calculating BMI.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SowmiyaShivakumar/Zero_Bootstrapper_Demo.git
   cd Zero_Bootstrapper_Demo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. Run the React frontend in another terminal.

### API Endpoint

- **POST** `/calculate_bmi`
  - Request body (JSON):
    ```json
    {
      "weight": 70,
      "height": 1.75
    }
    ```
  - Response:
    ```json
    {
      "bmi": 22.86
    }
    ```

### Usage

- Use the UI to input weight and height and calculate the BMI using the frontend.

## Authors

- Sowmiya Shivakumar

## License

This project is licensed under the MIT License.