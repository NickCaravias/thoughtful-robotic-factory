### Objective

Our robotic arm's sorting function has been a great success in Thoughtful's robotic automation factory. Now, customers want to understand how their packages will be processed upfront. They have sent us CSV files with package details.

Your task is to analyze these packages, apply the sorting criteria using your existing function, and generate a comprehensive report. This report will show how their packages will be sorted and help them understand the efficiency and capacity of our robotic arm.

This challenge builds upon your initial sorting function, expanding its capabilities to meet real-world demand.

### Task Details

**Plan** (5 - 10 minutes)

- Read the instructions below and plan execution

**Data Ingestion** (15 - 20 minutes)

- Write code to read the data from `packages.csv` (below) and store it in an appropriate data structure for processing.
- Handle any data inconsistencies, errors, or missing values gracefully.

**Data Analysis and Reporting** (15 - 20 minutes)

- **Calculate Statistics**:
    - Total number of packages that would be processed.
    - Number and percentage of packages in each stack (`STANDARD`, `SPECIAL`, `REJECTED`).
    - Average, minimum, and maximum `Mass` and `Volume` for each stack.
- **Generate Summary Report**:
    - Display the statistics in a clear and organized format.
    - Ensure the report is easy to read and understand.

**Q&A** (5-10 mins)

- Spend a few minutes discussing potential improvements to the solution
    - How to handle extremely large datasets
    - Ways to enhance performance further
    - Additional features that could be added

### Guidance

- **Resources**: You are allowed to look up syntax and documentation as needed during the exercise.
- **Evaluation Criteria**: Your work will be assessed on:
    - Functionality
    - Code quality
    - Pragmatic choices