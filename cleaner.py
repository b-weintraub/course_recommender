import pandas as pd

def cleaner(df):
    df['professor_name'] = df['tFname'] + ' ' + df['tLname']
    df.drop(['tFname','tMiddlename','tLname','Unnamed: 0','contentType','categoryType'], axis=1, inplace=True)
    df.dropna(inplace=True)
    df.rename(columns={"tDept": "Department"}, inplace=True)
    return df


def main():
    
    df = pd.read_csv('data/PC_data.csv')
    clean_data = cleaner(df)
    
    clean_data.to_csv('data/clean_data.csv')


if __name__ == '__main__':
    main()