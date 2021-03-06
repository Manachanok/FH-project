# Generated by Django 3.1.7 on 2021-03-21 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Building',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_code', models.CharField(max_length=30, unique=True)),
                ('department_name', models.CharField(default=None, max_length=40, null=True)),
                ('create_by', models.CharField(default=None, max_length=10, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_by', models.CharField(default=None, max_length=10, null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Department',
                'ordering': ['department_code'],
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.CharField(max_length=20)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.building')),
            ],
            options={
                'db_table': 'Floor',
                'ordering': ['site', 'building', 'floor'],
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('machine_id', models.AutoField(primary_key=True, serialize=False)),
                ('serial_id', models.CharField(default=None, max_length=50, null=True)),
                ('machine_production_line_code', models.CharField(default=None, max_length=30, null=True)),
                ('machine_name', models.CharField(blank=True, max_length=50)),
                ('machine_brand', models.CharField(blank=True, max_length=50)),
                ('machine_model', models.CharField(blank=True, max_length=50)),
                ('machine_supplier_code', models.CharField(blank=True, max_length=50)),
                ('machine_supplier_name', models.CharField(blank=True, max_length=50)),
                ('machine_supplier_contact', models.CharField(blank=True, max_length=50)),
                ('machine_eng_emp_id', models.CharField(blank=True, max_length=50)),
                ('machine_eng_emp_name', models.CharField(blank=True, max_length=50)),
                ('machine_eng_emp_contact', models.CharField(blank=True, max_length=50)),
                ('machine_pro_emp_id', models.CharField(blank=True, max_length=50)),
                ('machine_pro_emp_name', models.CharField(blank=True, max_length=50)),
                ('machine_pro_emp_contact', models.CharField(blank=True, max_length=50)),
                ('machine_load_capacity', models.CharField(blank=True, max_length=10)),
                ('machine_load_capacity_unit', models.CharField(blank=True, max_length=10)),
                ('machine_power_use_kwatt_per_hour', models.FloatField(blank=True, max_length=10)),
                ('machine_installed_datetime', models.DateField(default=None, null=True)),
                ('machine_start_use_datetime', models.DateField(default=None, null=True)),
                ('machine_hour', models.IntegerField(blank=True, default=None, null=True)),
                ('machine_hour_last_update', models.IntegerField(blank=True, default=None, null=True)),
                ('create_by', models.CharField(max_length=20)),
                ('create_date', models.DateField()),
                ('last_update_by', models.CharField(default=None, max_length=20, null=True)),
                ('last_update_date', models.DateField(default=None, null=True)),
                ('machine_image1', models.FileField(blank=True, null=True, upload_to='pictures/')),
                ('machine_image2', models.FileField(blank=True, null=True, upload_to='pictures/')),
                ('machine_image3', models.FileField(blank=True, null=True, upload_to='pictures/')),
                ('machine_image4', models.FileField(blank=True, null=True, upload_to='pictures/')),
                ('machine_image5', models.FileField(blank=True, null=True, upload_to='pictures/')),
                ('machine_document1', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('machine_document2', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('machine_document3', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('machine_document4', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('machine_document5', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('machine_details', models.CharField(blank=True, max_length=256)),
                ('machine_active', models.BooleanField()),
                ('machine_core', models.BooleanField()),
                ('machine_hour_update_date', models.DateField(default=None, null=True)),
                ('machine_asset_code', models.CharField(default=None, max_length=30, null=True)),
            ],
            options={
                'db_table': 'Machine_master',
                'ordering': ['line__production_line', 'machine_production_line_code'],
            },
        ),
        migrations.CreateModel(
            name='Machine_sparepart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_mtnchng_hour', models.IntegerField(blank=True, default=None, null=True)),
                ('last_mtnchk_hour', models.IntegerField(blank=True, default=None, null=True)),
                ('mtnchng_life_hour', models.IntegerField(blank=True, default=None, null=True)),
                ('mtnchk_life_hour', models.IntegerField(blank=True, default=None, null=True)),
                ('next_mtnchng_hour', models.IntegerField(blank=True, default=None, null=True)),
                ('next_mtnchk_hour', models.IntegerField(blank=True, default=None, null=True)),
                ('last_mtnchng_job_id', models.IntegerField(blank=True, default=None, null=True)),
                ('last_mtnchk_job_id', models.IntegerField(blank=True, default=None, null=True)),
                ('gen_mtnchng_date', models.DateField(blank=True, default=None, null=True)),
                ('gen_mtnchk_date', models.DateField(blank=True, default=None, null=True)),
                ('warning_hour', models.IntegerField(blank=True, default=None, null=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.machine')),
            ],
            options={
                'db_table': 'Machine_Sparepart',
                'ordering': ['machine', 'spare_part'],
            },
        ),
        migrations.CreateModel(
            name='Machine_type',
            fields=[
                ('mtype_id', models.AutoField(primary_key=True, serialize=False)),
                ('mtype_code', models.CharField(max_length=30)),
                ('mtype_name', models.CharField(max_length=50)),
                ('create_by', models.CharField(max_length=20)),
                ('create_date', models.DateField()),
                ('last_update_by', models.CharField(default=None, max_length=20, null=True)),
                ('last_update_date', models.DateField(default=None, null=True)),
            ],
            options={
                'db_table': 'Machine_type',
            },
        ),
        migrations.CreateModel(
            name='Maintenance_job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_no', models.CharField(max_length=25, unique=True)),
                ('job_gen_date', models.DateField(auto_now_add=True)),
                ('job_assign_date', models.DateField(default=None, null=True)),
                ('job_mtn_type', models.CharField(default=None, max_length=20, null=True)),
                ('job_result_type', models.CharField(default=None, max_length=20, null=True)),
                ('job_result_description', models.TextField(default=None, null=True)),
                ('job_fix_plan_hour', models.IntegerField(default=None, null=True)),
                ('job_mch_hour', models.IntegerField(default=None, null=True)),
                ('job_plan_hour', models.IntegerField(default=None, null=True)),
                ('job_report_date', models.DateField(default=None, null=True)),
                ('problem_cause', models.TextField(default=None, null=True)),
                ('corrective_action', models.TextField(default=None, null=True)),
                ('after_repair', models.TextField(default=None, null=True)),
                ('is_approve', models.BooleanField(default=False)),
                ('is_report', models.BooleanField(default=False)),
                ('job_status', models.CharField(default=None, max_length=30, null=True)),
                ('job_remark', models.TextField(default=None, null=True)),
                ('estimate_cost', models.PositiveIntegerField(default=None, null=True)),
                ('equipment_code1', models.TextField(default=None, null=True)),
                ('equipment_code2', models.TextField(default=None, null=True)),
                ('equipment_code3', models.TextField(default=None, null=True)),
                ('equipment_detail1', models.TextField(default=None, null=True)),
                ('equipment_detail2', models.TextField(default=None, null=True)),
                ('equipment_detail3', models.TextField(default=None, null=True)),
                ('equipment_quantity1', models.PositiveIntegerField(default=None, null=True)),
                ('equipment_quantity2', models.PositiveIntegerField(default=None, null=True)),
                ('equipment_quantity3', models.PositiveIntegerField(default=None, null=True)),
                ('equipment_note1', models.TextField(default=None, null=True)),
                ('equipment_note2', models.TextField(default=None, null=True)),
                ('equipment_note3', models.TextField(default=None, null=True)),
                ('job_approve_date', models.DateField(default=None, null=True)),
            ],
            options={
                'db_table': 'maintenance_job',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('org_id', models.AutoField(primary_key=True, serialize=False)),
                ('org_code', models.CharField(max_length=25)),
                ('org_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Organization',
            },
        ),
        migrations.CreateModel(
            name='Repair_and_maintenance_job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen_date', models.DateField(auto_now_add=True)),
                ('maintenance_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.maintenance_job')),
            ],
            options={
                'db_table': 'Repair_and_maintenance_job',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Role_management',
            },
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('screen_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('screen_name', models.CharField(max_length=40)),
                ('file_py', models.CharField(max_length=40)),
                ('file_html', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Screen_management',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Site',
            },
        ),
        migrations.CreateModel(
            name='Spare_part_group',
            fields=[
                ('spare_part_group_id', models.AutoField(primary_key=True, serialize=False)),
                ('spare_part_group_code', models.CharField(max_length=30)),
                ('spare_part_group_name', models.CharField(max_length=40)),
                ('create_by', models.CharField(max_length=20)),
                ('create_date', models.DateField()),
                ('last_update_by', models.CharField(default=None, max_length=20, null=True)),
                ('last_update_date', models.DateField(default=None, null=True)),
            ],
            options={
                'db_table': 'Spare_part_group',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
                ('create_by', models.CharField(max_length=10)),
                ('create_date', models.DateTimeField()),
                ('start_date', models.DateField()),
                ('expired_date', models.DateField()),
                ('expired_day', models.IntegerField(default=90)),
                ('update_by', models.CharField(default=None, max_length=10, null=True)),
                ('update_date', models.DateTimeField(default=None, null=True)),
                ('last_login_date', models.DateTimeField(default=None, null=True)),
                ('user_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'User_management',
            },
        ),
        migrations.CreateModel(
            name='User_and_department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_inform', models.BooleanField(default=None, null=True)),
                ('is_inspect', models.BooleanField(default=None, null=True)),
                ('is_approve', models.BooleanField(default=None, null=True)),
                ('is_receive', models.BooleanField(default=None, null=True)),
                ('is_assign', models.BooleanField(default=None, null=True)),
                ('is_report', models.BooleanField(default=None, null=True)),
                ('is_verify', models.BooleanField(default=None, null=True)),
                ('is_close', models.BooleanField(default=None, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.user')),
            ],
            options={
                'db_table': 'User_department',
                'ordering': ['department__department_code', 'user__firstname'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='departments',
            field=models.ManyToManyField(through='Machine_Management.User_and_department', to='Machine_Management.Department'),
        ),
        migrations.AddField(
            model_name='user',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.organization'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.role'),
        ),
        migrations.CreateModel(
            name='Spare_part_type',
            fields=[
                ('spare_part_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('spare_part_type_code', models.CharField(max_length=30)),
                ('spare_part_type_name', models.CharField(max_length=40)),
                ('create_by', models.CharField(max_length=20)),
                ('create_date', models.DateField()),
                ('last_update_by', models.CharField(default=None, max_length=20, null=True)),
                ('last_update_date', models.DateField(default=None, null=True)),
                ('spare_part_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.spare_part_group')),
            ],
            options={
                'db_table': 'Spare_part_type',
            },
        ),
        migrations.CreateModel(
            name='Spare_part_sub_type',
            fields=[
                ('spare_part_sub_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('spare_part_sub_type_code', models.CharField(max_length=30)),
                ('spare_part_sub_type_name', models.CharField(max_length=40)),
                ('create_by', models.CharField(max_length=20)),
                ('create_date', models.DateField()),
                ('last_update_by', models.CharField(default=None, max_length=20, null=True)),
                ('last_update_date', models.DateField(default=None, null=True)),
                ('spare_part_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.spare_part_type')),
            ],
            options={
                'db_table': 'Spare_part_sub_type',
                'ordering': ['spare_part_type'],
            },
        ),
        migrations.CreateModel(
            name='Spare_part',
            fields=[
                ('spare_part_id', models.AutoField(primary_key=True, serialize=False)),
                ('spare_part_name', models.CharField(blank=True, max_length=40)),
                ('spare_part_model', models.CharField(blank=True, max_length=40)),
                ('spare_part_brand', models.CharField(blank=True, max_length=40)),
                ('service_life', models.PositiveIntegerField(default=None, null=True)),
                ('service_plan_life', models.PositiveIntegerField(default=None, null=True)),
                ('create_by', models.CharField(max_length=20)),
                ('create_date', models.DateField()),
                ('last_update_by', models.CharField(default=None, max_length=20, null=True)),
                ('last_update_date', models.DateField(default=None, null=True)),
                ('spare_part_active', models.BooleanField(default=True)),
                ('spare_part_detail', models.TextField(blank=True, default=None, null=True)),
                ('spare_part_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.spare_part_group')),
                ('spare_part_sub_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.spare_part_sub_type')),
                ('spare_part_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.spare_part_type')),
            ],
            options={
                'db_table': 'Spare_part',
            },
        ),
        migrations.CreateModel(
            name='Role_Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_insert', models.CharField(max_length=5)),
                ('permission_update', models.CharField(max_length=5)),
                ('permission_delete', models.CharField(max_length=5)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.role')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.screen')),
            ],
            options={
                'db_table': 'Role_Screen',
                'ordering': ['role'],
            },
        ),
        migrations.AddField(
            model_name='role',
            name='members',
            field=models.ManyToManyField(through='Machine_Management.Role_Screen', to='Machine_Management.Screen'),
        ),
        migrations.CreateModel(
            name='Repair_notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repair_no', models.CharField(max_length=25, unique=True)),
                ('notification_date', models.DateField(default=None, null=True)),
                ('problem_report', models.TextField(default=None, null=True)),
                ('effect_problem', models.TextField(default=None, null=True)),
                ('use_date', models.DateField(default=None, null=True)),
                ('repair_status', models.CharField(default=None, max_length=30, null=True)),
                ('repair_gen_date', models.DateField(auto_now_add=True)),
                ('repair_close_date', models.DateField(default=None, null=True)),
                ('inspect_remark', models.TextField(default=None, null=True)),
                ('approve_remark', models.TextField(default=None, null=True)),
                ('receive_remark', models.TextField(default=None, null=True)),
                ('close_remark', models.TextField(default=None, null=True)),
                ('is_cancel', models.BooleanField(default=None, null=True)),
                ('is_inspect', models.BooleanField(default=None, null=True)),
                ('is_approve', models.BooleanField(default=None, null=True)),
                ('is_receive', models.BooleanField(default=None, null=True)),
                ('is_close', models.BooleanField(default=None, null=True)),
                ('can_close', models.BooleanField(default=False)),
                ('approve_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Machine_Management.user')),
                ('department_notifying', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Machine_Management.department')),
                ('department_receive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Machine_Management.department')),
                ('inspect_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Machine_Management.user')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.machine')),
                ('maintenance_jobs', models.ManyToManyField(through='Machine_Management.Repair_and_maintenance_job', to='Machine_Management.Maintenance_job')),
                ('receive_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Machine_Management.user')),
                ('repairer_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Machine_Management.user')),
            ],
            options={
                'db_table': 'repair_notice',
            },
        ),
        migrations.AddField(
            model_name='repair_and_maintenance_job',
            name='repair_notice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.repair_notice'),
        ),
        migrations.CreateModel(
            name='Production_line',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('production_line', models.IntegerField()),
                ('location_building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.building')),
                ('location_floor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.floor')),
                ('location_site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.site')),
            ],
            options={
                'db_table': 'Production_line',
                'ordering': ['location_site', 'location_building', 'production_line'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_code', models.CharField(max_length=30)),
                ('capacity', models.CharField(max_length=15)),
                ('labour', models.CharField(max_length=10)),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.production_line')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='org_line',
            field=models.ManyToManyField(to='Machine_Management.Production_line'),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('level', models.IntegerField()),
                ('parent_menu', models.CharField(default=None, max_length=30, null=True)),
                ('index', models.IntegerField()),
                ('path_url', models.CharField(default=None, max_length=30, null=True)),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.screen')),
            ],
            options={
                'db_table': 'Menu_management',
                'ordering': ['level', 'index'],
            },
        ),
        migrations.AddField(
            model_name='maintenance_job',
            name='job_assign_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Machine_Management.user'),
        ),
        migrations.AddField(
            model_name='maintenance_job',
            name='job_gen_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Machine_Management.user'),
        ),
        migrations.AddField(
            model_name='maintenance_job',
            name='job_mch_sp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.machine_sparepart'),
        ),
        migrations.AddField(
            model_name='maintenance_job',
            name='job_response_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Machine_Management.user'),
        ),
        migrations.CreateModel(
            name='Machine_subtype',
            fields=[
                ('subtype_id', models.AutoField(primary_key=True, serialize=False)),
                ('subtype_code', models.CharField(max_length=30)),
                ('subtype_name', models.CharField(max_length=50)),
                ('create_by', models.CharField(max_length=20)),
                ('create_date', models.DateField()),
                ('last_update_by', models.CharField(default=None, max_length=20, null=True)),
                ('last_update_date', models.DateField(default=None, null=True)),
                ('mch_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.machine_type')),
            ],
            options={
                'db_table': 'Machine_subtype',
            },
        ),
        migrations.AddField(
            model_name='machine_sparepart',
            name='spare_part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.spare_part'),
        ),
        migrations.CreateModel(
            name='Machine_capacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fg_batch_size', models.IntegerField(blank=True, default=None, null=True)),
                ('fg_batch_time', models.IntegerField(blank=True, default=None, null=True)),
                ('rm_name', models.CharField(max_length=30)),
                ('rm_batch_size', models.IntegerField(blank=True, default=None, null=True)),
                ('rm_unit', models.CharField(max_length=20)),
                ('fg_capacity', models.IntegerField(blank=True, default=None, null=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.machine')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.product')),
            ],
            options={
                'db_table': 'Machine_capacity',
            },
        ),
        migrations.AddField(
            model_name='machine',
            name='line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.production_line'),
        ),
        migrations.AddField(
            model_name='machine',
            name='mch_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.machine_type'),
        ),
        migrations.AddField(
            model_name='machine',
            name='sub_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.machine_subtype'),
        ),
        migrations.AddField(
            model_name='floor',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.site'),
        ),
        migrations.AddField(
            model_name='building',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine_Management.site'),
        ),
    ]
