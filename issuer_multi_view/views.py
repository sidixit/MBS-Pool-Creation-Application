from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django import forms
from issuer_multi_view.models import Issuer, Pool, Loan

# ========== Forms =========

class IssuerForm(ModelForm):
    class Meta:
        model = Issuer
        fields = ['name', 'email_address', 'initial_password', 'initial_role', 'company_name']

class LoginForm(forms.Form):
    id = forms.IntegerField(label = 'User ID')
    initial_password = forms.CharField(label='Password', max_length=100)

class PoolForm(ModelForm):
    class Meta:
        model = Pool
        fields = ['poolType','mortgageInterstRate','securityInterestRate','IssueDate','maturityDate','issuerId']

class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = ['loanNum', 'poolId', 'issuerId', 'activityDate', 'loanInterestRate','totalAmount','outstandingAmount']

# ========== Home =========

def home(request, template_name='issuer_multi_view/home.html'):
    issuer = Issuer.objects.all()
    ctx = {}
    ctx['issuer'] = issuer
    return render(request, template_name, ctx)

def pool_home(request, template_name='issuer_multi_view/pool_home.html'):
    pool = Pool.objects.all()
    ctx = {}
    ctx['pools'] = pool
    return render(request, template_name, ctx)

def loan_home(request, template_name='issuer_multi_view/loan_home.html'):
    loan = Loan.objects.all()
    ctx = {}
    ctx['loan'] = loan
    return render(request, template_name, ctx)


# ========== Issuer CRUD =========

def issuer_view(request, pk, template_name='issuer_multi_view/issuer_view.html'):
    issuer= get_object_or_404(Issuer, pk=pk)
    ctx = {}
    ctx["issuer"] = issuer
    return render(request, template_name, ctx)

def issuer_create(request, template_name='issuer_multi_view/issuer_form.html'):
    form = IssuerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('issuer_multi_view:home')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

def issuer_update(request, pk, template_name='issuer_multi_view/issuer_form.html'):
    issuer= get_object_or_404(Issuer, pk=pk)
    form = IssuerForm(request.POST or None, instance=issuer)
    if form.is_valid():
        form.save()
        return redirect('issuer_multi_view:home')
    ctx = {}
    ctx["form"] = form
    ctx["issuer"] = issuer
    return render(request, template_name, ctx)

def issuer_delete(request, pk, template_name='issuer_multi_view/issuer_confirm_delete.html'):
    issuer= get_object_or_404(Issuer, pk=pk)
    if request.method=='POST':
        issuer.delete()
        return redirect('issuer_multi_view:home')
    ctx = {}
    ctx["issuer"] = issuer
    return render(request, template_name, ctx)

# ========== Pool CRUD =========

def pool_view(request, pk, template_name='issuer_multi_view/pool_view.html'):
    pool= get_object_or_404(Pool, pk=pk)
    loan= Loan.objects.filter(poolId=pk)
    ctx = {}
    ctx["pool"] = pool
    ctx["loan"] = loan
    return render(request, template_name, ctx)

def pool_create(request, template_name='issuer_multi_view/pool_form.html'):
    form = PoolForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('issuer_multi_view:pool_home')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

def pool_update(request, pk, template_name='issuer_multi_view/pool_form.html'):
    pool= get_object_or_404(Pool, pk=pk)
    form = PoolForm(request.POST or None, instance=pool)
    if form.is_valid():
        form.save()
        return redirect('issuer_multi_view:pool_home')
    ctx = {}
    ctx["form"] = form
    ctx["pool"] = pool
    return render(request, template_name, ctx)

def pool_delete(request, pk, template_name='issuer_multi_view/pool_confirm_delete.html'):
    pool= get_object_or_404(Pool, pk=pk)
    if request.method=='POST':
        pool.delete()
        return redirect('issuer_multi_view:pool_home')
    ctx = {}
    ctx["pool"] = pool
    return render(request, template_name, ctx)

# ========== Loan CRUD =========

def loan_view(request, pk, template_name='issuer_multi_view/loan_view.html'):
    loan= get_object_or_404(Loan, pk=pk)
    ctx = {}
    ctx["loan"] = loan
    return render(request, template_name, ctx)

def loan_create(request, template_name='issuer_multi_view/loan_form.html'):
    form = LoanForm(request.POST or None)
    if form.is_valid():
        form.save()
        pk = form.cleaned_data['poolId']
        return redirect('issuer_multi_view:pool_view',pk)
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

def loan_update(request, pk, template_name='issuer_multi_view/loan_form.html'):
    loan= get_object_or_404(Loan, pk=pk)
    form = LoanForm(request.POST or None, instance=loan)
    if form.is_valid():
        form.save()
        return redirect('issuer_multi_view:loan_home')
    ctx = {}
    ctx["form"] = form
    ctx["loan"] = loan
    return render(request, template_name, ctx)

def loan_delete(request, pk, template_name='issuer_multi_view/loan_confirm_delete.html'):
    loan= get_object_or_404(Loan, pk=pk)
    if request.method=='POST':
        loan.delete()
        return redirect('issuer_multi_view:loan_home')
    ctx = {}
    ctx["loan"] = loan
    return render(request, template_name, ctx)


# ========== Login =========
def issuer_login(request, template_name='issuer_multi_view/login.html'):
    Issuers = Issuer.objects.all()
    form = LoginForm(request.POST or None)
    if form.is_valid():
        id = form.cleaned_data.get('id')
        password = form.cleaned_data.get('initial_password')
        for issuer in Issuers:
            if (issuer.id == id) and (issuer.initial_password==password):
                issuer_pools = Pool.objects.filter(issuerId=id).first()
                if issuer_pools is None:
                    return redirect('issuer_multi_view:pool_new')
                else:
                    return pool_view(request, id)

    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

def admin_login(request, template_name='issuer_multi_view/login.html'):
    Issuers = Issuer.objects.all()
    form = LoginForm(request.POST or None)
    if form.is_valid():
        id = form.cleaned_data.get('id')
        password = form.cleaned_data.get('initial_password')
        for issuer in Issuers:
            if (issuer.id == id) and (issuer.initial_password==password):
                issuer_pools = Pool.objects.filter(issuerId=id).first()
                if issuer_pools is None:
                    return redirect('issuer_multi_view:admin_home')
                else:
                    return redirect('home')

    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

# ========== Admin =========

def admin_home(request, template_name='issuer_multi_view/admin_home.html'):
    return render(request, template_name)
