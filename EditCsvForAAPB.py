import csv
import pandas as pd

# Using the def main() formatting allows you to write code in a module and then call it from other code you might write later, so you don't have to rewrite it again.
def main(): 
    
    # default='warn' to get rid of SettingWithCopyWarning
    pd.options.mode.chained_assignment = None  

    # Create a new dataframe from a csv file
    df = pd.read_csv('pandasTestData.csv')
    
    # Replace "nan" with blank
    df = df.fillna('')    
    
    # create a new dataframe 'subjects' with the subject column data. For data separated by a comma, split into multiple columns and give each column a sequentially named header, i.e. Subject1, Subject2
    df['Subject'] = df['Subject'].astype(str)
    subjects = pd.DataFrame(df['Subject'].str.split(',').tolist())
    subjects.columns = ['Subject' + str(col + 1) for col in subjects.columns]

    # create a new dataframe 'contributors' with the contributor column data. For data separated by a comma, split into multiple columns and give each column a sequentially named header, i.e. Contributor1, Contributor2
    df['Contributor'] = df['Contributor'].astype(str)    
    contributors = pd.DataFrame(df['Contributor'].str.split(',').tolist())
    contributors.columns = ['Contributor' + str(col + 1) for col in contributors.columns]
    
    # from the original dataframe 'df', keep specific columns which we will call 'new_df'
    keep_cols = ['Unique Identifier', 'Physical Format', 'Generations', 'Duration Physical', 'Storage Location',
                 'Date', 'Date Type', 'Item Title', 'Description','Publisher']
    new_df = df[keep_cols]
    
    # renaming column headers from original csv to specific AAPB header names
    newcols = {
    'Unique Identifier': 'Identifier', 
    'Duration Physical': 'Duration', 
    'Storage Location': 'Location',
    'Item Title': 'Title',
    }
    new_df.rename(columns=newcols, inplace=True)
   
    # add new columns and known values to the 'new_df' dataframe
    new_df['Identifier Source'] = 'KBOO item label'
    new_df['Media Type'] = 'Sound'
    new_df['Digital Format'] = 'audio/x-wav'
    new_df['Duration Approximate'] = 'Yes'
    new_df['Encoding'] = 'WAV'
    new_df['Publisher Role'] = 'Publisher'
    new_df['Subject Authority Used'] = 'KBOO Topic terms'
    new_df['Title Type'] = 'Supplied'
    
    # write the 'new_df' dataframe with a specific column order
    new_df = new_df[
        ['Identifier', 'Identifier Source', 'Media Type','Physical Format', 'Digital Format', 'Encoding', 'Generations', 'Duration','Duration Approximate',
         'Location', 'Date', 'Date Type', 'Title', 'Title Type','Description', 'Publisher',
         'Subject Authority Used']]   

    # join the subjects and contributors dataframes to the rest of the newly formatted data
    together = new_df.join(subjects)
    together = together.join(contributors)
    
    # write the data to a new csv
    together.to_csv('pandasTestExport.csv', index=False)

    # a visible, friendly alert in the command line that shows when the script has finished running
    print("All Done!")  
if __name__ == '__main__':
    main()