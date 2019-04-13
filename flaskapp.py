# import dependencies
import re
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import PeptideForm

app = Flask(__name__, template_folder='templates')

# decorator for user-input peptide analysis 
@app.route("/")
@app.route("/home", methods=['POST', 'GET'])
def home():

    # create variable to store form data
    form = PeptideForm()

    # conditional for user input 
    if form.validate_on_submit():
        return redirect(url_for('results'))

    # if user input invalid, remain in homepage
    else:
        return render_template('home.html', form=form)
    
# decorater to display peptide match results 
@app.route("/results", methods=['POST', 'GET'])
def results():

    # create variable to get form data
    form = PeptideForm()

    # create empty strings to hold peptide and protein sequences
    c1 = '' 
    p1 = ''

    c2 = ''
    p2 = ''

    # create variables to store peptide and protein sequences
    protein_ref = form.protein_seq.data
    peptide = form.peptide_seq.data

    # for loop to remove inappropriate spacing and set sequence to uppercase
    for char in protein_ref:
       c1 = char
       new_c = c1.upper().replace(" ", "").replace("\n", "").replace("\r", "")
       p1 = p1 + new_c

    for char in peptide: 
        c2 = char 
        new_c2 = c2.upper().replace(" ", "").replace("\n", "").replace("\r", "")
        p2 = p2 + new_c2

    # create variable to match peptide and protein sequence 
    match = re.search(p2, p1)

    # conditional for matching 
    if match: 

        # sucess message
        flash(f"Successful match for {form.protein_name.data}!", 'success')
    
        # calculations for start and end position 
        start_position = int(match.start() + 1)
        end_position = int(match.end())
        s = (start_position, end_position)

        # store peptide in new variable 
        p = p2

        # create variable to store PTM location
        m = int(form.phospho_site_location.data)

        # conditional to calculate PTM location 
        if m > 0: 
            t = (start_position - 1) + m 
        else: 
            t = None 

    # return error message if no matches, stay in homepage
    else:
        flash(f"No matches found. Please try again.", 'danger')
        return render_template('home.html', form=form)
    
    # return peptide match results in results page 
    return render_template('results.html', s=s, p=p, t=t)

# secret key hidden
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

# run application 
if __name__ == '__main__': 
    app.run(debug=True)


      