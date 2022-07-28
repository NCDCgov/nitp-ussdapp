from django.db import models

# Create your models here.

class Appadmin(models.Model):
    uid = models.AutoField(db_column='UID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    useremail = models.CharField(max_length=200)
    usertype = models.CharField(max_length=50)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'AppAdmin'


class Appsettings(models.Model):
    option_name = models.CharField(max_length=1000)
    option_value = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AppSettings'


class Appuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    org_name = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    fullname = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    last_activity_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'AppUser'


class Appuserbranch(models.Model):
    user_id = models.IntegerField()
    branch_id = models.IntegerField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'AppUserBranch'


class Branch(models.Model):
    name = models.CharField(max_length=100)
    sub_domain = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=1000, blank=True, null=True)
    phone = models.CharField(max_length=1000, blank=True, null=True)
    comment = models.CharField(max_length=4000, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Branch'


class Bulkmasterprocesses(models.Model):
    processid = models.AutoField(db_column='ProcessId', primary_key=True)  # Field name made lowercase.
    processname = models.TextField(db_column='ProcessName', blank=True, null=True)  # Field name made lowercase.
    privilegecode = models.TextField(db_column='PrivilegeCode', blank=True, null=True)  # Field name made lowercase.
    samplefilename = models.TextField(db_column='SampleFileName', blank=True, null=True)  # Field name made lowercase.
    approvalprocessid = models.BigIntegerField(db_column='ApprovalProcessId', blank=True, null=True)  # Field name made lowercase.
    workflowenabled = models.BooleanField(db_column='WorkflowEnabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BulkMasterProcesses'


class Bulkmasteruploaditemlog(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    bulkmasteruploadid = models.BigIntegerField(db_column='BulkMasterUploadId')  # Field name made lowercase.
    statusmsg = models.TextField(db_column='StatusMsg', blank=True, null=True)  # Field name made lowercase.
    a = models.TextField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    b = models.TextField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    c = models.TextField(db_column='C', blank=True, null=True)  # Field name made lowercase.
    d = models.TextField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    e = models.TextField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    f = models.TextField(db_column='F', blank=True, null=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    h = models.TextField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    i = models.TextField(db_column='I', blank=True, null=True)  # Field name made lowercase.
    j = models.TextField(db_column='J', blank=True, null=True)  # Field name made lowercase.
    k = models.TextField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    m = models.TextField(db_column='M', blank=True, null=True)  # Field name made lowercase.
    n = models.TextField(db_column='N', blank=True, null=True)  # Field name made lowercase.
    o = models.TextField(db_column='O', blank=True, null=True)  # Field name made lowercase.
    p = models.TextField(db_column='P', blank=True, null=True)  # Field name made lowercase.
    q = models.TextField(db_column='Q', blank=True, null=True)  # Field name made lowercase.
    r = models.TextField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    s = models.TextField(db_column='S', blank=True, null=True)  # Field name made lowercase.
    t = models.TextField(db_column='T', blank=True, null=True)  # Field name made lowercase.
    u = models.TextField(db_column='U', blank=True, null=True)  # Field name made lowercase.
    v = models.TextField(db_column='V', blank=True, null=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    x = models.TextField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    y = models.TextField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    z = models.TextField(db_column='Z', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BulkMasterUploadItemLog'


class Bulkmasteruploaditems(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    bulkmasteruploadid = models.BigIntegerField(db_column='BulkMasterUploadId')  # Field name made lowercase.
    statusmsg = models.TextField(db_column='StatusMsg', blank=True, null=True)  # Field name made lowercase.
    a = models.TextField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    b = models.TextField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    c = models.TextField(db_column='C', blank=True, null=True)  # Field name made lowercase.
    d = models.TextField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    e = models.TextField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    f = models.TextField(db_column='F', blank=True, null=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    h = models.TextField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    i = models.TextField(db_column='I', blank=True, null=True)  # Field name made lowercase.
    j = models.TextField(db_column='J', blank=True, null=True)  # Field name made lowercase.
    k = models.TextField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    m = models.TextField(db_column='M', blank=True, null=True)  # Field name made lowercase.
    n = models.TextField(db_column='N', blank=True, null=True)  # Field name made lowercase.
    o = models.TextField(db_column='O', blank=True, null=True)  # Field name made lowercase.
    p = models.TextField(db_column='P', blank=True, null=True)  # Field name made lowercase.
    q = models.TextField(db_column='Q', blank=True, null=True)  # Field name made lowercase.
    r = models.TextField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    s = models.TextField(db_column='S', blank=True, null=True)  # Field name made lowercase.
    t = models.TextField(db_column='T', blank=True, null=True)  # Field name made lowercase.
    u = models.TextField(db_column='U', blank=True, null=True)  # Field name made lowercase.
    v = models.TextField(db_column='V', blank=True, null=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    x = models.TextField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    y = models.TextField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    z = models.TextField(db_column='Z', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BulkMasterUploadItems'


class Bulkmasteruploads(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    processid = models.IntegerField(db_column='ProcessId')  # Field name made lowercase.
    refno = models.TextField(db_column='RefNo', blank=True, null=True)  # Field name made lowercase.
    itemcount = models.IntegerField(db_column='ItemCount')  # Field name made lowercase.
    initiatedby = models.TextField(db_column='InitiatedBy', blank=True, null=True)  # Field name made lowercase.
    dateinitiated = models.DateTimeField(db_column='DateInitiated')  # Field name made lowercase.
    iscomplete = models.BooleanField(db_column='IsComplete')  # Field name made lowercase.
    datecompleted = models.DateTimeField(db_column='DateCompleted', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.TextField(db_column='IPAddress', blank=True, null=True)  # Field name made lowercase.
    initiatoruserid = models.BigIntegerField(db_column='InitiatorUserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BulkMasterUploads'


class Logos(models.Model):
    branch_id = models.IntegerField()
    logo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Logos'


class Partners(models.Model):
    partnerid = models.AutoField(db_column='partnerID', primary_key=True)  # Field name made lowercase.
    partnername = models.CharField(db_column='partnerName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pdatecreated = models.DateTimeField(db_column='pdateCreated', blank=True, null=True)  # Field name made lowercase.
    partnerkey = models.TextField(db_column='partnerKey', blank=True, null=True)  # Field name made lowercase.
    partnerstatus = models.CharField(db_column='partnerStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Partners'


class Testresult(models.Model):
    id = models.BigAutoField(primary_key=True)
    otp = models.TextField(blank=True, null=True)
    epidno = models.TextField(blank=True, null=True)
    labid = models.TextField(blank=True, null=True)
    refby = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    other_name = models.TextField(blank=True, null=True)
    sampling_date = models.DateTimeField(blank=True, null=True)
    reported_date = models.DateTimeField(blank=True, null=True)
    testname = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    methodology = models.TextField(blank=True, null=True)
    sample_type = models.TextField(blank=True, null=True)
    result_comment = models.TextField(blank=True, null=True)
    clinical_utility = models.TextField(blank=True, null=True)
    interpretation = models.TextField(blank=True, null=True)
    limitation = models.TextField(blank=True, null=True)
    counselling = models.TextField(blank=True, null=True)
    date_uploaded = models.DateTimeField()
    uploaded_by = models.TextField(blank=True, null=True)
    reviewer_comment = models.TextField(blank=True, null=True)
    date_approved = models.DateTimeField(blank=True, null=True)
    approved_by = models.TextField(blank=True, null=True)
    filepath = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    email = models.TextField(blank=True, null=True)
    cert_no = models.TextField(blank=True, null=True)
    passport_no = models.TextField(blank=True, null=True)
    log_status = models.IntegerField()
    phone = models.TextField(blank=True, null=True)
    passport_pic = models.TextField(blank=True, null=True)
    intl_passport = models.TextField(blank=True, null=True)
    refno = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    payt_ref = models.TextField(blank=True, null=True)
    amount_due = models.DecimalField(max_digits=18, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=18, decimal_places=2)
    payment_date = models.DateTimeField(blank=True, null=True)
    payment_status = models.IntegerField()
    payt_channel = models.TextField(blank=True, null=True)
    payt_remarks = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_home_service = models.IntegerField(blank=True, null=True)
    is_travel = models.IntegerField(blank=True, null=True)
    is_repeat = models.IntegerField(blank=True, null=True)
    voucher_no = models.TextField(blank=True, null=True)
    voucher_amount = models.DecimalField(max_digits=18, decimal_places=2)
    branch_id = models.IntegerField(blank=True, null=True)
    token = models.CharField(max_length=1000, blank=True, null=True)
    sampling_time = models.CharField(max_length=1000, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TestResult'


class Testresultviewlog(models.Model):
    id = models.BigAutoField(primary_key=True)
    mode = models.TextField(blank=True, null=True)
    epidno = models.TextField(blank=True, null=True)
    otp = models.TextField(blank=True, null=True)
    testresult_id = models.BigIntegerField()
    viewed_by = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField()
    status = models.BooleanField()
    old_data = models.TextField(blank=True, null=True)
    new_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TestResultViewLog'


class Ussdphonelist(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    org_name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'USSDPhoneList'


class Voucher(models.Model):
    id = models.BigAutoField(primary_key=True)
    serialno = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    is_active = models.BooleanField()
    is_used = models.BooleanField()
    used_by_test_id = models.BigIntegerField()
    user_fullname = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Voucher'