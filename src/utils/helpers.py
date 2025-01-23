def save_report(report, filename='research_report.txt'):
    '''
    Save the final report to a file.
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)
