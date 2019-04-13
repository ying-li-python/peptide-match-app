# import dependencies and flask-wtf extension for forms 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

# create class for peptide analysis 
class PeptideForm(FlaskForm): 
    protein_name = StringField('Protein Name', validators=[DataRequired(), Length(min=2)])
    protein_seq = TextAreaField('Reference Protein Sequence', validators=[DataRequired(), Length(min=2)])
    peptide_seq = TextAreaField('Peptide Sequence', validators=[DataRequired(), Length(min=2)])
    phospho_site_location = StringField('PTM site location', validators=[DataRequired()])
    
    submit = SubmitField('Submit')