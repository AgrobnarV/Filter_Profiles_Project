**Requirements for task**
Write a CLI program that filters profiles that meet a condition.

**Profile**
A profile is a description of a person's career path. A profile contains the following:
1. Name
2. Surname
3. List of skills (strings) that the person possesses. These are typically all the skills from all the work experiences below.
4. About me. Free text that the person uses to describe themselves.
5. Current location. Country + city
6. Experience, an unordered list consisting of elements:
   - Company name
   - Position
   - Short description of what the candidate did in this position
   - Skills that they used in this position
   - Start date of work at this company
   - End date of work at this company. Can be empty, which means that the candidate is currently working in this position.
   - Location. Country and city

All dates are in the format YYYY-MM-DD. If a person worked in multiple places at the same time, we count this as one experience. For example, if they worked in two places in 2020, we still count that year as one year of experience, not two.
The repository contains a file containing a pydantic profile schema. This schema must be used for deserialization.
The list of profiles must be a JSON file located in the project.

**Task Details**
Prepare two verification functions:
    1. Experienced Python developer
        Worked at a FAANG company in one of the last two work experiences
        Position in the last three work experiences: Backend developer or Software engineer
        Total experience of more than 8 years
        Worked with Python and C++ in the last position
        Lives in London

[//]: # (    2. Middle UX designer)
[//]: # (        Worked as a Product designer or UX designer or similar in two &#40;or one if the company is one&#41; of the last work experiences)
[//]: # (        Possesses Figma, Sketch, UX-research, Miro &#40;any two&#41;)
[//]: # (        Lives in the European Union)
[//]: # (        Experience in the last work experience of more than two years)
[//]: # (        Total experience of less than five years)

The "last places" above refer to time.
Therefore, you also need to order the experience by start date. Ideally, this should be done in the pydantic schema.

**Interface**
The program should be launched from the console as follows:
python <your entry point> --filter <chosen filter> --input <file_name>

**Parameters**
- chosen filter: A parameter that selects one of the checks.
- file_name: The file with the list of profiles (positive + negative scenarios).

**Output**
For each profile in file_name, the status of the check is printed to the console:
# ($ python3 <args>)
# (John Smith – True)
# (Elon Musk – False, Not enough experience)
# (Steve Jobs – False, Never worked in UK)

**Values**
- True: The check passed
- False, reason: The check failed, reason is the reason (if there are several reasons, one is enough).

**Technical limitations**
- Python 3.7+
- Only built-in modules, except for the following:
  - pydantic==1.7.3

**Todo**
1. Can check that names are made up only of letters, and dates begin in 1900.
2. Can verify that the values in the different fields of the JSON objects are consistent. 
Can verify that the programming language specified in the skills field corresponds to the programming language specified in the skills_position field.
3. Add the ability to specify multiple filtering criteria.
4. Add option to format output in more convenient way
5. Add comments to explain complex parts of your code. 
   - Also, consider adding docstrings to functions, classes, and modules to provide documentation.
6. Consider using a CLI framework like Click or argparse to make your CLI more powerful and user-friendly.
7. If the program becomes more complex, consider using a configuration file to manage settings and parameters.
8. Write unit tests to ensure that each function and class behaves as expected.
9. Write assertion test through pytest
10. Instead of relying on string comparison for filters, consider using an Enum to define available filters
11. Add new filters and skills for UX designer or QA designer or Project Manager. Add new companies in #faang_companies