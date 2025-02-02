#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# import the needed libraries/packages
import logging              # helps with nicely-formatted output
import time                 # lets us calculate how long the script took
import pandas as pd         # all sorts of data wrangling features
import jinja2               # lets us generate our reports
from xhtml2pdf import pisa  # helps us create PDF reports


# define globals/contants
DATA_FILE="DD - Expiry Subscription Church List Email Report.csv"
TEMPLATE="template.html"

# Utility function
def convert_html_to_pdf(source_html, output_filename):
    with open(output_filename, "w+b") as result_file:
        pisa_status = pisa.CreatePDF(source_html, dest=result_file)
    return pisa_status.err


def create_report():

    # read the csv into a dataframe
    df = pd.read_csv(DATA_FILE, na_filter=False)

    # clean up the data a little
    # let's convert *all* the fields to strings
    df = df.astype(str)
    # note: you generally *won't* want to do this... you can do individual colums like this:
    # df['LastName'] = df['LastName'].astype(str)
    df['Quantity'] = df['Quantity'].astype(int)
    # or multiple fields...
    # df[['LastName', 'FirstName']] = df[['LastName', 'FirstName']].astype(str)

    # get a list of distinct account numbers
    accounts = df["Account"].unique()

    # loop through those accounts...
    for account in accounts:

        logging.info(f"Generating report for account {account}")

        # data structure for the report
        context = {'account_num': account}

        # get the rows from the data frame for the current account
        account_rows = df[df['Account'] == account]

        # sort the rows by LastName then FirstName then SubscriberCompanyName
        sorted = account_rows.sort_values(['LastName', 'FirstName', 'SubscriberCompanyName'])        

        # sum the quantity field and add it to the report context
        context['quantity'] = sorted['Quantity'].sum()

        # add the data rows to the report context
        context['data_rows'] = sorted.to_dict(orient='records')

        # grab the first row to get some data we need for the report context
        row0 = sorted.iloc[0]
        context['name'] = row0['Name']
        context['address'] = row0['Address']
        context['address2'] = row0['Address2']
        context['city'] = row0['City']
        context['state'] = row0['State']
        context['zip'] = row0['Zip']

        # generate the account report
        output_filename = f"reports/{account}_{context['name'].replace(',', '').replace(' ', '_')}.pdf"

        # load the template and munge it with the data
        template_loader = jinja2.FileSystemLoader('./')
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template(TEMPLATE)
        source_html = template.render(context)

        # create the pdf
        convert_html_to_pdf(source_html, output_filename)


def main():
    """ Primary Entry-point for program """

    # setup logging information so we get some nicely-formatted output
    logging.basicConfig(format='[%(asctime)s] %(levelname)s %(message)s', level=logging.INFO)
    logging.info('** Sample Report Generation Utility **')
    start_time = time.time()
  
    # actually generate the report    
    create_report()

    logging.info("Script Finished")
    logging.info("Elapsed Time: %s seconds ", (time.time() - start_time))


# stub to call the main if this script file is called 
# by itself (vs. being included into a different script)
if __name__ == '__main__':
    main()
