import pandas as pd


def main():
#    pd.options.mode.chained_assignment = None  # default='warn'
    
    df = pd.read_csv('search_results_metadata_import.csv')

    keep_cols = ['Unique Identifier', 'Physical Format', 'Generations', 'Duration Physical', 'Storage Location',
                 'Date', 'Date Type', 'Item Title', 'Asset Type', 'Description', 'Subject', 'Contributor', 'Publisher']

    new_df = df[keep_cols]
    new_df.rename(columns={'Duration Physical': 'Duration', 'Storage Location': 'Location', 'Item Title': 'Title'}, inplace=True)
    new_df['Identifier Source'] = 'KBOO item label'
    new_df['Media Type'] = 'Sound'
    new_df['Digital Format'] = 'audio/x-wav'
    new_df['Duration Approximate'] = 'Yes'
    new_df['Encoding'] = 'WAV'
    new_df['Publisher Role'] = 'Publisher'
    new_df['Subject Authority Used'] = 'KBOO Topic terms'
    new_df['Title Type'] = 'Supplied'
    new_df = new_df[
        ['Unique Identifier', 'Identifier Source', 'Physical Format', 'Digital Format', 'Encoding', 'Generations', 'Duration',
         'Location', 'Date', 'Date Type', 'Title', 'Title Type', 'Asset Type', 'Description', 'Subject',
         'Subject Authority Used', 'Contributor', 'Publisher']]
    new_df['Subject'] = new_df['Subject'].astype(str)    
    subjects = pd.DataFrame(new_df['Subject'].str.split(',').tolist())
    subjects.columns = ['Subject' + str(col) for col in subjects.columns]
    
    new_df['Contributor'] = new_df['Contributor'].astype(str)    
    contributors = pd.DataFrame(new_df['Contributor'].str.split(',').tolist())
    contributors.columns = ['Contributor' + str(col) for col in contributors.columns]
    
    together = new_df.join(subjects)
    together = together.join(contributors)
    
    together.to_csv('aapb-test-data-export.csv', index=False)


if __name__ == '__main__':
    main()