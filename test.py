import PyPDF2
import re
import pandas as pd
# Open the PDF file


file_name = 'test.pdf'
with open(file_name, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    number_of_pages = len(reader.pages)
    print(f'The PDF has {number_of_pages} pages.')

   
    text = ''
    for page in range(number_of_pages):
        page_text = reader.pages[page].extract_text()
        if page_text:
            text += page_text + '\n'  # Add a newline for clarity


trip_pattern = r'(\d{2}[A-Za-z]{3}\d{4})\s+(\d{12})\s+(\w+)\s+(\d{2}:\d{2}:\d{2})(\d{2}:\d{2}:\d{2})\s+([\w/\s]+)\s+\$(\d+\.\d{2})'

trip_matches = re.findall(trip_pattern, text)

data = []
print("\nTrip Details:")
def create_df(trip_matches):
    
    for match in trip_matches:
        date, tag, vehicle_class, time, finish_time, details, amount = match
        print(f" Tag: {tag},Date: {date}, Vehicle Class: {vehicle_class}, Start Time: {time}, Finish Time: {finish_time}, Details: {details}, Amount: {amount}")
        data.append({
            'PDF Name': file_name,
            'Date': date,
            'Tag': tag,
            'Time': time,
            'Amount': amount
        })
    df = pd.DataFrame(data)


    return df

dataframe = create_df(trip_matches)
print(dataframe)