from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=10, required=False)
    website = forms.URLField(required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}), max_length=200, required=False)
    state = forms.ChoiceField(choices=[('', ''), ('1', 'ANDAMAN AND NICOBAR ISLANDS'), ('2', 'ANDHRA PRADESH'), ('3', 'ARUNACHAL PRADESH'), ('4', 'ASSAM'), ('5', 'BIHAR'), ('6', 'CHANDIGARH'), ('7', 'DADRA & NAGAR HAVELI'), ('8', 'DAMAN & DIU'), ('9', 'DELHI'), ('10', 'GOA'), ('11', 'GUJARAT'), ('12', 'HARYANA'), ('13', 'HIMACHAL PRADESH'), ('14', 'JAMMU AND KASHMIR'), ('15', 'KARNATAKA'), ('16', 'KERALA'), ('17', 'LAKHSWADEEP'), ('18', 'MADHYA PRADESH'), ('19', 'MAHARASHTRA'), ('20', 'MANIPUR'), ('21', 'MEGHALAYA'), ('22', 'MIZORAM'), ('23', 'NAGALAND'), ('24', 'ORISSA'), ('25', 'PONDICHERRY'), ('26', 'PUNJAB'), ('27', 'RAJASTHAN'), ('28', 'SIKKIM'), ('29', 'TAMIL NADU'), ('30', 'TRIPURA'), ('31', 'UTTAR PRADESH'), ('32', 'WEST BENGAL'), ('33', 'CHHATTISGARH'), ('34', 'UTTARKHAND'), ('35', 'JHARKHAND'), ('36', 'UNION TERRITORY'), ('37', 'TELANGANA'), ('98', 'APO')])
    partner_id = forms.CharField(max_length=20, required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['email'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['phone'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['website'].widget.attrs.update({'autocomplete': 'off'})


class User_Detail(forms.Form):
    uid = forms.CharField(max_length=50,required=True)
    fname = forms.CharField(max_length=50,required=True)
    mname = forms.CharField(max_length=50)
    lname = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)

