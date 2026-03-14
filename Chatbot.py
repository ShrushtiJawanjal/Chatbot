import tkinter as tk
from tkinter import scrolledtext, ttk
import re
from thefuzz import process

# ----------------- Utility Functions -----------------

def is_math_expression(query):
    """Check if the query is a mathematical expression."""
    return re.fullmatch(r'[0-9+\-*/(). ]+', query) is not None

def evaluate_math_expression(expression):
    """Safely evaluate mathematical expressions."""
    try:
        return str(eval(expression))
    except Exception:
        return "Sorry, I couldn't calculate that."

# ----------------- Q&A Database -----------------

qa_database = {
"What are AI problems?": "AI problems include pathfinding, knowledge representation, decision-making, and learning from data.",

"What is the Tic-Tac-Toe problem in AI?": "It is a classic example used to demonstrate game-playing AI, often solved using Minimax or Alpha-Beta pruning.",

"What are Production Systems in AI?": "A Production System consists of a set of rules and a working memory, used in AI for problem-solving.",

"What is Knowledge Representation in AI?": "It refers to techniques used to represent information in a way that AI systems can use to reason.",

"What are Search Strategies in AI?": "AI search strategies include uninformed (BFS, DFS) and informed (A*, AO*) techniques.",

"What is an AND-OR graph?": "An AND-OR graph is used in AI for representing decision problems with dependencies.",

"What is Data Science?": "Data Science is the study of data to extract insights using statistics, AI, and computing.",

"What is Deep Learning?": "Deep Learning is a subset of ML that uses neural networks with multiple layers.",

"What is Power BI?": "Power BI is a business analytics tool used to visualize data and share insights.",
    
"What is Artificial Intelligence?": "Artificial Intelligence is the simulation of human intelligence in machines that can think, learn, and solve problems.",

"What is Machine Learning?": "Machine Learning is a subset of AI that allows systems to learn patterns from data and improve automatically.",

"What is Supervised Learning?": "Supervised learning is a machine learning method where models are trained using labeled data.",

"What is Unsupervised Learning?": "Unsupervised learning is a method where models find hidden patterns in data without labeled outputs.",

"What is Reinforcement Learning?": "Reinforcement learning is a learning technique where an agent learns by receiving rewards or penalties.",

"What is a Neural Network?": "A neural network is a computing model inspired by the human brain used to recognize patterns.",

"What is Natural Language Processing?": "Natural Language Processing is a field of AI that enables computers to understand human language.",

"What is Computer Vision?": "Computer Vision is an AI field that allows machines to interpret and analyze images or videos.",

"What is an AI Agent?": "An AI agent is a system that perceives its environment and takes actions to achieve goals.",

"What is a Heuristic in AI?": "A heuristic is a rule or method used to make problem-solving faster in AI.",

"What is Breadth First Search (BFS)?": "BFS is a search algorithm that explores nodes level by level.",

"What is Depth First Search (DFS)?": "DFS is a search algorithm that explores nodes deeply before moving to another branch.",

"What is A* Search Algorithm?": "A* is an informed search algorithm that finds the shortest path using heuristics.",

"What is a Knowledge Base?": "A knowledge base stores facts and rules used by AI systems.",

"What is an Expert System?": "An expert system is an AI program that imitates the decision-making ability of a human expert.",

"What is Big Data?": "Big Data refers to extremely large datasets that require advanced tools for processing.",

"What is Data Mining?": "Data mining is the process of discovering patterns and knowledge from large datasets.",

"What is Data Visualization?": "Data visualization is the graphical representation of data using charts and graphs.",

"What is Data Cleaning?": "Data cleaning is the process of removing errors and inconsistencies from data.",

"What is a Dataset?": "A dataset is a structured collection of related data used for analysis.",

"What is a Dashboard in Power BI?": "A dashboard in Power BI is a single page that displays multiple visualizations.",

"What is a Report in Power BI?": "A report in Power BI is a collection of charts and visuals created from a dataset.",

"What is Power BI Desktop?": "Power BI Desktop is a tool used to create reports and dashboards.",

"What is Power BI Service?": "Power BI Service is a cloud platform used to share and collaborate on reports.",

"What is a Slicer in Power BI?": "A slicer is a visual filter used to interactively filter data in reports.",

"What is DAX in Power BI?": "DAX stands for Data Analysis Expressions used to create formulas and calculations in Power BI.",

"What is a KPI?": "KPI stands for Key Performance Indicator used to measure performance.",

"What is a Bar Chart?": "A bar chart is a graph that represents data using rectangular bars.",

"What is a Pie Chart?": "A pie chart is a circular chart that shows data as parts of a whole.",

"What is a Line Chart?": "A line chart displays trends over time using connected data points.",

"What is a Table in Power BI?": "A table is a structured format of rows and columns used to store data.",

"What is Data Modeling in Power BI?": "Data modeling is the process of creating relationships between tables.",

"What is Data Transformation?": "Data transformation converts data into a suitable format for analysis.",

"What is ETL?": "ETL stands for Extract, Transform, and Load process used for data integration.",

"What is Business Intelligence?": "Business Intelligence refers to technologies used to analyze business data and support decision making.",
"What is a Neural Network?": "A neural network is a computing system inspired by the human brain used for pattern recognition.",

"What is Big Data Analytics?": "Big Data Analytics analyzes extremely large datasets to discover patterns and trends.",

"What is a Data Pipeline?": "A data pipeline is a set of processes that move and transform data from source to destination.",

"What is Power Query in Power BI?": "Power Query is used to connect, clean, and transform data before analysis.",

"What is DirectQuery in Power BI?": "DirectQuery allows Power BI to query data directly from the data source without importing it.",

"What is Import Mode in Power BI?": "Import Mode loads data into Power BI so it can be analyzed quickly.",

"What is Row Level Security in Power BI?": "Row Level Security restricts data access for different users in Power BI reports.",

"What is a Semantic Model?": "A semantic model organizes data in a way that makes analysis easier for users.",
"What is a Data Source?": "A data source is where the data originates, like Excel, SQL Server, or an API.",

"What is Data Cleaning?": "Data cleaning is fixing or removing incorrect, incomplete, or inconsistent data.",

"What is Data Transformation?": "Data transformation is changing data into a format suitable for analysis.",

"What is a Dataset?": "A dataset is a structured collection of related data used for reporting and analysis.",

"What is Data Modeling?": "Data modeling defines relationships between tables to make analysis easier.",

"What is a Relationship in Power BI?": "A relationship connects tables based on common columns to allow joined analysis.",

"What is Row Level Security (RLS)?": "RLS restricts data access for different users based on roles or permissions.",

"What is a Measure?": "A measure is a calculation created using DAX that summarizes data dynamically.",

"What is a Calculated Column?": "A calculated column is a new column created using a formula applied to each row.",

"What is Aggregation?": "Aggregation summarizes data using operations like SUM, COUNT, AVG, MIN, or MAX.",

"What is a Filter in Power BI?": "A filter displays only data that meets certain conditions in visuals.",

"What is a Slicer in Power BI?": "A slicer is an interactive filter allowing users to select specific subsets of data.",

"What is a KPI?": "KPI (Key Performance Indicator) shows how well a metric is performing against a target.",

"What is a Dashboard in Power BI?": "A dashboard is a single-page view containing multiple visuals for quick insights.",

"What is a Report in Power BI?": "A report is a multi-page collection of visuals created from datasets.",

"What is Drill Down / Drill Through?": "Drill down allows exploration of hierarchical data; drill through navigates to detail pages.",

"What is Power Query?": "Power Query is used to connect, clean, and transform data before analysis.",

"What is DAX?": "DAX (Data Analysis Expressions) is used for calculations and aggregations in Power BI.",

"What is Data Refresh?": "Data refresh updates your dataset with the latest data from the source.",

"What is DirectQuery vs Import Mode?": "DirectQuery queries data live from the source; Import Mode loads data into Power BI for faster analysis.",

"What is a Gateway in Power BI?": "A gateway connects on-premises data sources to Power BI Service in the cloud.",

"What is Data Profiling?": "Data profiling examines data quality, distributions, and patterns before analysis.",

"What is ETL?": "ETL (Extract, Transform, Load) is the process of moving data from sources to a database or warehouse.",

"What is a Data Warehouse?": "A data warehouse stores large volumes of structured data optimized for analysis.",

"What is Metadata?": "Metadata is data about the data, like column names, data types, or source info.",

"What is a Hierarchy in Power BI?": "Hierarchy organizes fields in levels, like Year > Quarter > Month > Day.",

"What is Quick Insights?": "Quick Insights automatically finds trends and patterns in a dataset.",

"What is Q&A in Power BI?": "Q&A allows users to ask questions in natural language and get visual answers.",

"What is Conditional Formatting in Power BI?": "Conditional formatting changes the appearance of visuals based on data values.",

"What is a Bookmark in Power BI?": "A bookmark saves the current view of a report including filters and visuals.",

"What is an AI Visual in Power BI?": "AI visuals, like Key Influencers or Decomposition Tree, use AI to identify patterns in data.",

"What is a Template in Power BI?": "A template is a pre-built Power BI report that can be reused with different data.",

"What is Column Quality / Column Distribution?": "These are Power Query features that help check completeness, errors, and value distribution in a column.",

"What is a Custom Visual in Power BI?": "A custom visual is an add-on visualization that provides additional functionality beyond built-in visuals.",

"What is Usage Metrics in Power BI?": "Usage metrics show how reports and dashboards are being viewed and interacted with by users.",
"What is Power BI Desktop?": "Power BI Desktop is a Windows application used to create reports and data models.",

"What is Power BI Service?": "Power BI Service is the cloud-based platform where you can publish and share reports.",

"What is Power BI Mobile?": "Power BI Mobile allows you to view and interact with reports on mobile devices.",

"What is a Power BI Dashboard?": "A dashboard is a single-page view containing multiple visuals for quick insights.",

"What is a Power BI Report?": "A report is a collection of visualizations built from datasets in Power BI.",

"What is a Dataset in Power BI?": "A dataset is a collection of data imported or connected to Power BI for analysis.",

"What is a Data Model in Power BI?": "A data model defines relationships between different tables in Power BI.",

"What is a Table in Power BI?": "A table is a structured collection of rows and columns representing data.",

"What is a Column in Power BI?": "A column is a vertical set of data values in a table.",

"What is a Row in Power BI?": "A row is a single record in a table containing values for each column.",

"What is a Relationship in Power BI?": "A relationship connects two tables through a common column for analysis.",

"What is Table Relationship Cardinality in Power BI?": "Cardinality defines how tables are related, e.g., one-to-one or one-to-many.",

"What is Hierarchy in Power BI?": "Hierarchy allows organizing fields in levels like Year > Month > Day.",

"What is a Visual in Power BI?": "A visual is a graphical representation of data like charts, maps, or cards.",

"What is a Card Visual?": "A card visual shows a single important metric, like total sales.",

"What is a Column Chart?": "A column chart displays data using vertical bars for comparison.",

"What is a Stacked Column Chart?": "A stacked column chart shows parts of a whole across categories.",

"What is a Bar Chart in Power BI?": "A bar chart represents data using horizontal bars for easy comparison.",

"What is a Line Chart in Power BI?": "A line chart shows trends over time using connected points.",

"What is a Pie Chart in Power BI?": "A pie chart represents data as parts of a whole.",

"What is a Scatter Plot in Power BI?": "A scatter plot shows the relationship between two numerical variables.",

"What is a Map Visual in Power BI?": "A map visual displays geographic data on a map.",

"What is a KPI Visual in Power BI?": "A KPI visual shows progress toward a target or goal.",

"What is a Slicer in Power BI?": "A slicer is an interactive filter that lets users select specific data.",

"What is a Filter in Power BI?": "A filter displays only the data that meets certain conditions in a visual.",

"What is Power Query in Power BI?": "Power Query is used to connect, transform, and prepare data for analysis.",

"What is Query Editor in Power BI?": "Query Editor allows cleaning and transforming data before loading into Power BI.",

"What is DAX in Power BI?": "DAX stands for Data Analysis Expressions used to create formulas and calculations.",

"What is a Measure in Power BI?": "A measure is a calculation performed on your data using DAX.",

"What is a Calculated Column in Power BI?": "A calculated column is a new column added to a table based on a formula.",

"What is Data Refresh in Power BI?": "Data refresh updates your dataset with the latest data from the source.",

"What is a Gateway in Power BI?": "A gateway connects on-premise data sources to Power BI in the cloud.",

"What is Row Level Security (RLS) in Power BI?": "RLS restricts data access for different users based on their roles.",

"What is Power BI Publish?": "Publishing sends your Power BI report from Desktop to the Power BI Service.",

"What is Power BI Workspace?": "A workspace is a collaborative environment for creating and sharing reports.",

"What is Power BI App?": "A Power BI App packages dashboards and reports for easy sharing with users.",

"What is Bookmarks in Power BI?": "Bookmarks save a specific view of a report including filters and slicers.",

"What is Drill Through in Power BI?": "Drill through allows users to click on a data point and see related details on another page.",

"What is Drill Down in Power BI?": "Drill down lets users explore hierarchical data by expanding or collapsing levels.",

"What is Q&A in Power BI?": "Q&A allows users to ask natural language questions and get answers in visuals.",

"What is Quick Insights in Power BI?": "Quick Insights automatically analyzes a dataset to find patterns and trends.",

"What is Template in Power BI?": "A template is a pre-built Power BI file that can be reused with different data.",

"What is Power BI AI Visuals?": "AI visuals like Key Influencers use AI to identify patterns and drivers in your data."
}



# ----------------- Matching Function -----------------

def find_best_match(user_question):
    result = process.extractOne(user_question, qa_database.keys())
    if result and result[1] > 70:
        return result[0]
    return None

# ----------------- Chat Function -----------------

def get_response():
    user_input = user_entry.get().strip()

    if user_input.lower() == "exit":
        root.destroy()
        return

    if user_input:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"\nYou: {user_input}\n", "user")

        if is_math_expression(user_input):
            response = evaluate_math_expression(user_input)
        else:
            matched_question = find_best_match(user_input)
            response = qa_database.get(
                matched_question,
                "Sorry, I can only answer AI and Data Science-related questions."
            )

        chat_window.insert(tk.END, f"Chatbot: {response}\n", "bot")
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)
        user_entry.delete(0, tk.END)

# ----------------- GUI -----------------

root = tk.Tk()
root.title("Smart Chatbot")
root.geometry("450x550")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="P R Pote Patil College of Engineering",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title_label.pack(pady=5)

welcome_label = tk.Label(
    root,
    text="Welcome to AI Chatbot",
    font=("Arial", 12),
    fg="white",
    bg="#1e1e1e"
)
welcome_label.pack(pady=5)

chat_window = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=50,
    height=20,
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 12)
)
chat_window.config(state=tk.DISABLED)
chat_window.tag_configure("user", foreground="#00ff7f", font=("Arial", 12, "bold"))
chat_window.tag_configure("bot", foreground="#00bfff", font=("Arial", 12))
chat_window.pack(pady=10, padx=10)

user_entry = tk.Entry(
    root,
    width=45,
    font=("Arial", 12),
    bg="#3b3b3b",
    fg="white",
    insertbackground="white"
)
user_entry.pack(pady=5, padx=10)
user_entry.bind("<Return>", lambda event: get_response())

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=5)

send_button = ttk.Button(button_frame, text="Send", command=get_response)
send_button.grid(row=0, column=0, padx=5)

close_button = ttk.Button(button_frame, text="Close", command=root.destroy)
close_button.grid(row=0, column=1, padx=5)

root.mainloop()