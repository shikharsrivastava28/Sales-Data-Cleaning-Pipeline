<h1>1. Project Title & Goal</h1>

<h3>Project Title : Sales Data Cleaner (ETL using Pandas)</h3>
<h4>Goal : This project reads a messy sales CSV file, cleans and deduplicates the data, converts prices from USD to INR, and exports the result as a structured JSON file.</h4>

<h1>2. Setup Instructions</h1>

<h3>Step 1: Install dependencies</h3>
pip install pandas

<h3>Step 2: Run the script</h3>
python main.py
<h5>Note: Make sure sales.csv is present in the same directory before running the script.</h5>

<h1>3. The Logic (How I thought)</h1>

<h4>Why did I choose this approach?</h4>
<h5>I chose Pandas-only ETL because:</h5>
<li>Pandas provides a clean and efficient way to handle CSV data.</li>
<li>String cleaning, type conversion, deduplication, and transformations can be done in very few readable lines.</li>
<li>This approach is scalable and commonly used in real-world data analytics and data engineering workflows.</li>

<h5>The ETL flow I followed:</h5>

<li><b>Extract</b>: Load CSV using pd.read_csv()</li>
<li><b>Transform</b>: Clean symbols, convert data types, remove duplicates, and apply currency conversion</li>
<li><b>Load</b>: Export the final clean data to JSON using to_json()</li>

<h6>This keeps the pipeline simple, readable, and professional.</h6>

<h4>What was the hardest bug I faced, and how did I fix it?</h4>

<h5>The hardest issue was converting the price column to float because:</h5>

<li>Some values had a $ sign</li>
<li>Some values were quoted</li>
<li>Pandas initially treated the column as object (string)</li>

<b>Fix:</b>

<h5>I cleaned the column step-by-step before conversion:</h5>

<li>Removed $ using string replacement</li>

<li>Ensured all values were strings</li>

<li>Converted the cleaned values to float</li>

<h6>This ensured consistent numeric conversion and prevented runtime errors.</h6>

<h1>4. Output Screenshots:</h1>
<img width="1105" height="846" alt="image" src="https://github.com/user-attachments/assets/cebe03e2-626c-4aa9-8450-46b0820c8198" />

<h1>5. Future Improvements (If I had 2 more days)</h1>

<h4>If I had more time, I would:</h4>

<li>Add data validation (missing values, invalid prices, negative values)</li>
<li>Introduce logging instead of print statements</li>
<li>Refactor the script into modular ETL functions</li>
<li>Add unit tests using pytest</li>
<li>Make the currency rate configurable via a config file</li>
<li>Handle large datasets and performance optimization</li>
<li>Add better documentation and sample datasets</li>

