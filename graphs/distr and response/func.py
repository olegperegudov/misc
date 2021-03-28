def plot_cat_distribution(cat, train_df=train_df):
    ax = plt.subplots(figsize=(12, 6))
    sns.set_style('whitegrid')
    sns.countplot(x=cat, data=train_df)
    plt.ylabel('No. of Observations', size=20)
    plt.xlabel(cat+' Count', size=20)
    plt.show()


def plot_cat_response(cat, train_df=train_df):
    ax = plt.subplots(figsize=(8, 5))
    sns.set_style('whitegrid')
    sns.countplot(x=cat, hue='target', data=train_df)
    plt.show()
