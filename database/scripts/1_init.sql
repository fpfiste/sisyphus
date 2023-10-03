-- public.asset_absence_codes definition

-- Drop table

-- DROP TABLE public.asset_absence_codes;

CREATE TABLE public.asset_absence_codes (
	id_asset_absence_code int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	asset_absence_code varchar(30) NOT NULL,
	asset_absence_code_abbreviation varchar(5) NOT NULL,
	CONSTRAINT asset_absence_codes_pkey PRIMARY KEY (id_asset_absence_code)
);


-- public.asset_types definition

-- Drop table

-- DROP TABLE public.asset_types;

CREATE TABLE public.asset_types (
	id_asset_type int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	asset_type varchar(50) NOT NULL,
	CONSTRAINT asset_types_pkey PRIMARY KEY (id_asset_type)
);


-- public.auth_group definition

-- Drop table

-- DROP TABLE public.auth_group;

CREATE TABLE public.auth_group (
	id int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	"name" varchar(150) NOT NULL,
	CONSTRAINT auth_group_name_key UNIQUE (name),
	CONSTRAINT auth_group_pkey PRIMARY KEY (id)
);
CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


-- public.auth_user definition

-- Drop table

-- DROP TABLE public.auth_user;

CREATE TABLE public.auth_user (
	id int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	"password" varchar(128) NOT NULL,
	last_login timestamptz NULL,
	is_superuser bool NOT NULL,
	username varchar(150) NOT NULL,
	first_name varchar(150) NOT NULL,
	last_name varchar(150) NOT NULL,
	email varchar(254) NOT NULL,
	is_staff bool NOT NULL,
	is_active bool NOT NULL,
	date_joined timestamptz NOT NULL,
	CONSTRAINT auth_user_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_username_key UNIQUE (username)
);
CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


-- public.clearing_type definition

-- Drop table

-- DROP TABLE public.clearing_type;

CREATE TABLE public.clearing_type (
	id_clearing_type int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	clearing_type varchar(50) NOT NULL,
	CONSTRAINT clearing_type_pk PRIMARY KEY (id_clearing_type),
	CONSTRAINT clearing_type_un UNIQUE (clearing_type)
);


-- public.countries definition

-- Drop table

-- DROP TABLE public.countries;

CREATE TABLE public.countries (
	id_country int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	country varchar(50) NOT NULL,
	country_code varchar(3) NOT NULL,
	CONSTRAINT countries_pk PRIMARY KEY (id_country),
	CONSTRAINT countries_un UNIQUE (country)
);


-- public.currencies definition

-- Drop table

-- DROP TABLE public.currencies;

CREATE TABLE public.currencies (
	id_currency int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	currency varchar(50) NOT NULL,
	currency_abbreviation varchar(3) NOT NULL,
	currency_account_nr varchar(50) NOT NULL,
	CONSTRAINT currencies_pkey PRIMARY KEY (id_currency)
);


-- public.django_content_type definition

-- Drop table

-- DROP TABLE public.django_content_type;

CREATE TABLE public.django_content_type (
	id int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	app_label varchar(100) NOT NULL,
	model varchar(100) NOT NULL,
	CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model),
	CONSTRAINT django_content_type_pkey PRIMARY KEY (id)
);


-- public.django_migrations definition

-- Drop table

-- DROP TABLE public.django_migrations;

CREATE TABLE public.django_migrations (
	id int8 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	app varchar(255) NOT NULL,
	"name" varchar(255) NOT NULL,
	applied timestamptz NOT NULL,
	CONSTRAINT django_migrations_pkey PRIMARY KEY (id)
);


-- public.django_session definition

-- Drop table

-- DROP TABLE public.django_session;

CREATE TABLE public.django_session (
	session_key varchar(40) NOT NULL,
	session_data text NOT NULL,
	expire_date timestamptz NOT NULL,
	CONSTRAINT django_session_pkey PRIMARY KEY (session_key)
);
CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


-- public.employee_absence_codes definition

-- Drop table

-- DROP TABLE public.employee_absence_codes;

CREATE TABLE public.employee_absence_codes (
	id_employee_absence_code int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	employee_absence_code varchar(50) NOT NULL,
	employee_absence_code_abbreviation varchar(5) NOT NULL,
	CONSTRAINT employee_absence_codes_pkey PRIMARY KEY (id_employee_absence_code)
);


-- public.employee_types definition

-- Drop table

-- DROP TABLE public.employee_types;

CREATE TABLE public.employee_types (
	id_employee_type int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	employee_type_description varchar(50) NOT NULL,
	CONSTRAINT employee_types_pkey PRIMARY KEY (id_employee_type)
);


-- public.invoice_states definition

-- Drop table

-- DROP TABLE public.invoice_states;

CREATE TABLE public.invoice_states (
	id_invoice_state int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	invoice_state varchar(20) NOT NULL,
	CONSTRAINT invoice_states_pkey PRIMARY KEY (id_invoice_state)
);


-- public.invoice_terms definition

-- Drop table

-- DROP TABLE public.invoice_terms;

CREATE TABLE public.invoice_terms (
	id_invoice_term int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	due_days int4 NOT NULL,
	term_title varchar(20) NOT NULL,
	CONSTRAINT invoice_terms_due_days_key UNIQUE (due_days),
	CONSTRAINT invoice_terms_pkey PRIMARY KEY (id_invoice_term)
);


-- public.sales_state definition

-- Drop table

-- DROP TABLE public.sales_state;

CREATE TABLE public.sales_state (
	id_sales_state int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	sales_state varchar(20) NOT NULL,
	CONSTRAINT sales_state_pkey PRIMARY KEY (id_sales_state),
	CONSTRAINT sales_state_sales_state_key UNIQUE (sales_state)
);
CREATE INDEX sales_state_sales_state_a193d641_like ON public.sales_state USING btree (sales_state varchar_pattern_ops);


-- public.sys_rec_states definition

-- Drop table

-- DROP TABLE public.sys_rec_states;

CREATE TABLE public.sys_rec_states (
	id_sys_rec_status int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	sys_rec_status varchar(20) NOT NULL,
	entity varchar(20) NULL,
	CONSTRAINT sys_rec_states_pkey PRIMARY KEY (id_sys_rec_status)
);


-- public.task_states definition

-- Drop table

-- DROP TABLE public.task_states;

CREATE TABLE public.task_states (
	id_task_state int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	task_state varchar(20) NOT NULL,
	CONSTRAINT task_states_pkey PRIMARY KEY (id_task_state)
);


-- public.template_types definition

-- Drop table

-- DROP TABLE public.template_types;

CREATE TABLE public.template_types (
	id_template_type int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	template_type varchar(50) NOT NULL,
	CONSTRAINT sales_template_pk PRIMARY KEY (id_template_type)
);


-- public.templates definition

-- Drop table

-- DROP TABLE public.templates;

CREATE TABLE public.templates (
	id_template int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	fk_project int4 NULL,
	amount numeric(11, 2) NULL,
	unit_price numeric(11, 2) NULL,
	description varchar(200) NULL,
	fk_currency int4 NULL,
	fk_unit int4 NULL,
	fk_vat int4 NULL,
	fk_template_type int4 NULL,
	template_title varchar(50) NOT NULL,
	CONSTRAINT task_templates_pkey PRIMARY KEY (id_template)
);
CREATE INDEX task_templates_fk_currency_315f0c49 ON public.templates USING btree (fk_currency);
CREATE INDEX task_templates_fk_unit_69400482 ON public.templates USING btree (fk_unit);
CREATE INDEX task_templates_fk_vat_12a8af6b ON public.templates USING btree (fk_vat);


-- public.units definition

-- Drop table

-- DROP TABLE public.units;

CREATE TABLE public.units (
	id_unit int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	unit varchar(20) NOT NULL,
	unit_abbreviation varchar(5) NOT NULL,
	CONSTRAINT units_pkey PRIMARY KEY (id_unit)
);


-- public.vat definition

-- Drop table

-- DROP TABLE public.vat;

CREATE TABLE public.vat (
	id_vat int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	vat numeric(3, 3) NOT NULL,
	vat_title varchar(50) NOT NULL,
	CONSTRAINT vat_pkey PRIMARY KEY (id_vat),
	CONSTRAINT vat_vat_key UNIQUE (vat)
);


-- public.auth_permission definition

-- Drop table

-- DROP TABLE public.auth_permission;

CREATE TABLE public.auth_permission (
	id int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	"name" varchar(255) NOT NULL,
	content_type_id int4 NOT NULL,
	codename varchar(100) NOT NULL,
	CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename),
	CONSTRAINT auth_permission_pkey PRIMARY KEY (id),
	CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


-- public.auth_user_groups definition

-- Drop table

-- DROP TABLE public.auth_user_groups;

CREATE TABLE public.auth_user_groups (
	id int8 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	user_id int4 NOT NULL,
	group_id int4 NOT NULL,
	CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id),
	CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


-- public.auth_user_user_permissions definition

-- Drop table

-- DROP TABLE public.auth_user_user_permissions;

CREATE TABLE public.auth_user_user_permissions (
	id int8 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	user_id int4 NOT NULL,
	permission_id int4 NOT NULL,
	CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id),
	CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


-- public.authtoken_token definition

-- Drop table

-- DROP TABLE public.authtoken_token;

CREATE TABLE public.authtoken_token (
	"key" varchar(40) NOT NULL,
	created timestamptz NOT NULL,
	user_id int4 NOT NULL,
	CONSTRAINT authtoken_token_pkey PRIMARY KEY (key),
	CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id),
	CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


-- public.companies definition

-- Drop table

-- DROP TABLE public.companies;

CREATE TABLE public.companies (
	id_company int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	company_name varchar(50) NOT NULL,
	company_street varchar(50) NOT NULL,
	company_zipcode varchar(50) NOT NULL,
	fk_country int4 NOT NULL,
	company_city varchar(50) NOT NULL,
	company_internal_alias varchar(50) NOT NULL,
	company_email varchar(50) NULL,
	is_customer bool NULL,
	is_supplier bool NULL,
	is_subcontractor bool NULL,
	fk_sys_rec_status int4 NOT NULL,
	company_custom_fields jsonb NULL,
	is_own_company bool NULL,
	CONSTRAINT companies_company_internal_alias_key UNIQUE (company_internal_alias),
	CONSTRAINT companies_pkey PRIMARY KEY (id_company),
	CONSTRAINT companies_fk FOREIGN KEY (fk_country) REFERENCES public.countries(id_country),
	CONSTRAINT companies_fk_sys_rec_status_d804c5ea_fk_sys_rec_s FOREIGN KEY (fk_sys_rec_status) REFERENCES public.sys_rec_states(id_sys_rec_status) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX companies_company_internal_alias_47763c3e_like ON public.companies USING btree (company_internal_alias varchar_pattern_ops);
CREATE INDEX companies_fk_sys_rec_status_d804c5ea ON public.companies USING btree (fk_sys_rec_status);


-- public.django_admin_log definition

-- Drop table

-- DROP TABLE public.django_admin_log;

CREATE TABLE public.django_admin_log (
	id int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	action_time timestamptz NOT NULL,
	object_id text NULL,
	object_repr varchar(200) NOT NULL,
	action_flag int2 NOT NULL,
	change_message text NOT NULL,
	content_type_id int4 NULL,
	user_id int4 NOT NULL,
	CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0)),
	CONSTRAINT django_admin_log_pkey PRIMARY KEY (id),
	CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


-- public.employees definition

-- Drop table

-- DROP TABLE public.employees;

CREATE TABLE public.employees (
	id_employee int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	employee_first_name varchar(50) NOT NULL,
	employee_last_name varchar(50) NOT NULL,
	employee_street varchar(50) NOT NULL,
	employee_zipcode varchar(20) NOT NULL,
	employee_city varchar(50) NOT NULL,
	employee_email varchar(50) NULL,
	employee_cell_phone varchar(50) NULL,
	employee_birthday date NULL,
	employee_salary numeric(11, 2) NULL,
	employee_fte numeric(3, 2) NULL,
	employee_internal_alias varchar(10) NOT NULL,
	fk_employee_type int4 NOT NULL,
	fk_sys_rec_status int4 NOT NULL,
	fk_country int4 NOT NULL,
	employee_custom_fields jsonb NULL,
	fk_company int4 NOT NULL,
	CONSTRAINT employees_employee_internal_alias_key UNIQUE (employee_internal_alias),
	CONSTRAINT employees_pkey PRIMARY KEY (id_employee),
	CONSTRAINT employees_fk FOREIGN KEY (fk_country) REFERENCES public.countries(id_country),
	CONSTRAINT employees_fk_company FOREIGN KEY (fk_company) REFERENCES public.companies(id_company),
	CONSTRAINT employees_fk_employee_type_236e57e4_fk_employee_ FOREIGN KEY (fk_employee_type) REFERENCES public.employee_types(id_employee_type) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT employees_fk_sys_rec_status_f319e4a4_fk_sys_rec_s FOREIGN KEY (fk_sys_rec_status) REFERENCES public.sys_rec_states(id_sys_rec_status) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX employees_employee_internal_alias_5fdb54d3_like ON public.employees USING btree (employee_internal_alias varchar_pattern_ops);
CREATE INDEX employees_fk_employee_type_236e57e4 ON public.employees USING btree (fk_employee_type);
CREATE INDEX employees_fk_sys_rec_status_f319e4a4 ON public.employees USING btree (fk_sys_rec_status);


-- public.invoice_text_templates definition

-- Drop table

-- DROP TABLE public.invoice_text_templates;

CREATE TABLE public.invoice_text_templates (
	id_invoice_text int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	invoice_text varchar(200) NOT NULL,
	fk_customer int4 NOT NULL,
	invoice_text_title varchar(20) NOT NULL,
	CONSTRAINT invoice_texts_pkey PRIMARY KEY (id_invoice_text),
	CONSTRAINT invoice_texts_fk_customer_765c2502_fk_companies_id_company FOREIGN KEY (fk_customer) REFERENCES public.companies(id_company) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX invoice_texts_fk_customer_765c2502 ON public.invoice_text_templates USING btree (fk_customer);


-- public.payables definition

-- Drop table

-- DROP TABLE public.payables;

CREATE TABLE public.payables (
	id_payable int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	fk_company int4 NOT NULL,
	invoice_date date NOT NULL,
	net_total numeric(11, 2) NOT NULL,
	vat numeric(11, 2) NOT NULL,
	fk_invoice_status int4 NOT NULL DEFAULT 1,
	fk_terms int4 NOT NULL,
	fk_currency int4 NOT NULL,
	positions jsonb NULL,
	invoice_id varchar(200) NOT NULL,
	total numeric(11, 2) NOT NULL,
	CONSTRAINT payables_pk PRIMARY KEY (id_payable),
	CONSTRAINT payables_un UNIQUE (invoice_id),
	CONSTRAINT payables_fk FOREIGN KEY (fk_currency) REFERENCES public.currencies(id_currency),
	CONSTRAINT payables_fk_1 FOREIGN KEY (fk_company) REFERENCES public.companies(id_company),
	CONSTRAINT payables_fk_2 FOREIGN KEY (fk_invoice_status) REFERENCES public.invoice_states(id_invoice_state),
	CONSTRAINT payables_fk_3 FOREIGN KEY (fk_terms) REFERENCES public.invoice_terms(id_invoice_term)
);


-- public.projects definition

-- Drop table

-- DROP TABLE public.projects;

CREATE TABLE public.projects (
	id_project int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	project_name varchar(200) NOT NULL,
	start_date date NOT NULL,
	end_date date NOT NULL,
	fk_customer int4 NOT NULL,
	fk_sys_rec_status int4 NOT NULL,
	project_custom_fields jsonb NULL,
	CONSTRAINT projects_pkey PRIMARY KEY (id_project),
	CONSTRAINT projects_fk FOREIGN KEY (fk_sys_rec_status) REFERENCES public.sys_rec_states(id_sys_rec_status),
	CONSTRAINT projects_fk_customer_32d0f6c7_fk_companies_id_company FOREIGN KEY (fk_customer) REFERENCES public.companies(id_company) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX projects_fk_customer_32d0f6c7 ON public.projects USING btree (fk_customer);


-- public.receivables definition

-- Drop table

-- DROP TABLE public.receivables;

CREATE TABLE public.receivables (
	id_invoice int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	invoice_date date NOT NULL,
	invoice_text varchar(200) NULL,
	fk_invoice_state int4 NOT NULL,
	fk_invoice_terms int4 NOT NULL,
	fk_vat int4 NOT NULL,
	net_total numeric(11, 2) NOT NULL,
	total numeric(11, 2) NOT NULL,
	fk_currency int4 NOT NULL,
	fk_project int4 NOT NULL,
	discount numeric(3, 3) NULL,
	CONSTRAINT invoices_pkey PRIMARY KEY (id_invoice),
	CONSTRAINT invoices_fk FOREIGN KEY (fk_vat) REFERENCES public.vat(id_vat),
	CONSTRAINT invoices_fk_1 FOREIGN KEY (fk_currency) REFERENCES public.currencies(id_currency),
	CONSTRAINT invoices_fk_invoice_state_e9e847ba_fk_invoice_s FOREIGN KEY (fk_invoice_state) REFERENCES public.invoice_states(id_invoice_state) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT invoices_fk_invoice_terms_3036695b_fk_invoice_t FOREIGN KEY (fk_invoice_terms) REFERENCES public.invoice_terms(id_invoice_term) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT invoices_fk_project FOREIGN KEY (fk_project) REFERENCES public.projects(id_project)
);
CREATE INDEX invoices_fk_invoice_state_e9e847ba ON public.receivables USING btree (fk_invoice_state);
CREATE INDEX invoices_fk_invoice_terms_3036695b ON public.receivables USING btree (fk_invoice_terms);


-- public.sales definition

-- Drop table

-- DROP TABLE public.sales;

CREATE TABLE public.sales (
	id_sale int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	sale_date date NOT NULL,
	amount numeric(11, 2) NOT NULL,
	unit_price numeric(11, 2) NOT NULL,
	customer_reference varchar(50) NULL,
	description varchar(200) NOT NULL,
	sale_time time NOT NULL,
	fk_currency int4 NOT NULL,
	fk_invoice int4 NULL,
	fk_project int4 NOT NULL,
	fk_sales_status int4 NOT NULL,
	fk_unit int4 NOT NULL,
	fk_vat int4 NOT NULL,
	sale_custom_fields jsonb NULL,
	fk_clearing_type int4 NOT NULL,
	CONSTRAINT sales_pkey PRIMARY KEY (id_sale),
	CONSTRAINT sales_fk FOREIGN KEY (fk_clearing_type) REFERENCES public.clearing_type(id_clearing_type),
	CONSTRAINT sales_fk_currency_43dcbc47_fk_currencies_id_currency FOREIGN KEY (fk_currency) REFERENCES public.currencies(id_currency) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT sales_fk_invoice_0a9cd917_fk_invoices_id_invoice FOREIGN KEY (fk_invoice) REFERENCES public.receivables(id_invoice) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT sales_fk_project_7d42e2cf_fk_projects_id_project FOREIGN KEY (fk_project) REFERENCES public.projects(id_project) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT sales_fk_sales_status_28a5058c_fk_sales_state_id_sales_state FOREIGN KEY (fk_sales_status) REFERENCES public.sales_state(id_sales_state) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT sales_fk_unit_5b0e8c1b_fk_units_id_unit FOREIGN KEY (fk_unit) REFERENCES public.units(id_unit) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT sales_fk_vat_461b945f_fk_vat_id_vat FOREIGN KEY (fk_vat) REFERENCES public.vat(id_vat) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX sales_fk_currency_43dcbc47 ON public.sales USING btree (fk_currency);
CREATE INDEX sales_fk_invoice_0a9cd917 ON public.sales USING btree (fk_invoice);
CREATE INDEX sales_fk_project_7d42e2cf ON public.sales USING btree (fk_project);
CREATE INDEX sales_fk_sales_status_28a5058c ON public.sales USING btree (fk_sales_status);
CREATE INDEX sales_fk_unit_5b0e8c1b ON public.sales USING btree (fk_unit);
CREATE INDEX sales_fk_vat_461b945f ON public.sales USING btree (fk_vat);


-- public.assets definition

-- Drop table

-- DROP TABLE public.assets;

CREATE TABLE public.assets (
	id_asset int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	asset_description varchar(50) NOT NULL,
	asset_internal_alias varchar(20) NOT NULL,
	fk_asset_type int4 NOT NULL,
	fk_sys_rec_status int4 NOT NULL,
	asset_custom_fields jsonb NULL,
	fk_company int4 NOT NULL,
	CONSTRAINT assets_pkey PRIMARY KEY (id_asset),
	CONSTRAINT assets_fk FOREIGN KEY (fk_company) REFERENCES public.companies(id_company),
	CONSTRAINT assets_fk_asset_type_88e64c56_fk_asset_types_id_asset_type FOREIGN KEY (fk_asset_type) REFERENCES public.asset_types(id_asset_type) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT assets_fk_sys_rec_status_9f557fd4_fk_sys_rec_s FOREIGN KEY (fk_sys_rec_status) REFERENCES public.sys_rec_states(id_sys_rec_status) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX assets_fk_asset_type_88e64c56 ON public.assets USING btree (fk_asset_type);
CREATE INDEX assets_fk_sys_rec_status_9f557fd4 ON public.assets USING btree (fk_sys_rec_status);


-- public.auth_group_permissions definition

-- Drop table

-- DROP TABLE public.auth_group_permissions;

CREATE TABLE public.auth_group_permissions (
	id int8 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	group_id int4 NOT NULL,
	permission_id int4 NOT NULL,
	CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id),
	CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


-- public.cancellations definition

-- Drop table

-- DROP TABLE public.cancellations;

CREATE TABLE public.cancellations (
	id_invoice_cancellation int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	cancellation_date date NOT NULL,
	cancellation_time time NOT NULL,
	cancellation_reason varchar(200) NOT NULL,
	cancellation_user varchar(20) NOT NULL,
	fk_invoice int4 NOT NULL,
	CONSTRAINT invoice_cancellation_pk PRIMARY KEY (id_invoice_cancellation),
	CONSTRAINT invoice_cancellation_un UNIQUE (fk_invoice),
	CONSTRAINT invoice_cancellation_fk FOREIGN KEY (fk_invoice) REFERENCES public.receivables(id_invoice)
);


-- public.employee_absences definition

-- Drop table

-- DROP TABLE public.employee_absences;

CREATE TABLE public.employee_absences (
	id_employee_absence int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	employee_absence_date_from date NOT NULL,
	employee_absence_date_to date NOT NULL,
	fk_employee int4 NOT NULL,
	fk_employee_absence_code int4 NOT NULL,
	employee_absence_time_from time NOT NULL,
	employee_absence_time_to time NOT NULL,
	CONSTRAINT employee_absences_pkey PRIMARY KEY (id_employee_absence),
	CONSTRAINT employee_absences_fk_employee_absence__0f106f50_fk_employee_ FOREIGN KEY (fk_employee_absence_code) REFERENCES public.employee_absence_codes(id_employee_absence_code) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT employee_absences_fk_employee_d330c4d2_fk_employees_id_employee FOREIGN KEY (fk_employee) REFERENCES public.employees(id_employee) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX employee_absences_fk_employee_absence_code_0f106f50 ON public.employee_absences USING btree (fk_employee_absence_code);
CREATE INDEX employee_absences_fk_employee_d330c4d2 ON public.employee_absences USING btree (fk_employee);


-- public.tasks definition

-- Drop table

-- DROP TABLE public.tasks;

CREATE TABLE public.tasks (
	id_task int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	task_date_from date NULL,
	task_date_to date NULL,
	amount numeric(11, 2) NULL,
	unit_price numeric(11, 2) NULL,
	description varchar(200) NOT NULL,
	internal_info varchar(200) NULL,
	customer_reference varchar(100) NULL,
	task_time_from time NULL,
	task_time_to time NULL,
	fk_asset_1 int4 NULL,
	fk_asset_2 int4 NULL,
	fk_currency int4 NULL,
	fk_employee_1 int4 NULL,
	fk_employee_2 int4 NULL,
	fk_invoice int4 NULL,
	fk_project int4 NOT NULL,
	fk_task_state int4 NOT NULL,
	fk_unit int4 NULL,
	fk_vat int4 NULL,
	task_custom_fields jsonb NULL,
	fk_clearing_type int4 NULL,
	CONSTRAINT tasks_pkey PRIMARY KEY (id_task),
	CONSTRAINT tasks_fk FOREIGN KEY (fk_clearing_type) REFERENCES public.clearing_type(id_clearing_type),
	CONSTRAINT tasks_fk_asset_1_477b32a9_fk_assets_id_asset FOREIGN KEY (fk_asset_1) REFERENCES public.assets(id_asset) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_asset_2_96e85ef9_fk_assets_id_asset FOREIGN KEY (fk_asset_2) REFERENCES public.assets(id_asset) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_currency_96170cc9_fk_currencies_id_currency FOREIGN KEY (fk_currency) REFERENCES public.currencies(id_currency) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_employee_1_c9b198a4_fk_employees_id_employee FOREIGN KEY (fk_employee_1) REFERENCES public.employees(id_employee) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_employee_2_1169876b_fk_employees_id_employee FOREIGN KEY (fk_employee_2) REFERENCES public.employees(id_employee) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_invoice_ea3beb60_fk_invoices_id_invoice FOREIGN KEY (fk_invoice) REFERENCES public.receivables(id_invoice) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_project_fee5c3c8_fk_projects_id_project FOREIGN KEY (fk_project) REFERENCES public.projects(id_project) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_task_state_a8407fe2_fk_task_states_id_task_state FOREIGN KEY (fk_task_state) REFERENCES public.task_states(id_task_state) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_unit_acfa1ab8_fk_units_id_unit FOREIGN KEY (fk_unit) REFERENCES public.units(id_unit) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_vat_486022be_fk_vat_id_vat FOREIGN KEY (fk_vat) REFERENCES public.vat(id_vat) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX tasks_fk_asset_1_477b32a9 ON public.tasks USING btree (fk_asset_1);
CREATE INDEX tasks_fk_asset_2_96e85ef9 ON public.tasks USING btree (fk_asset_2);
CREATE INDEX tasks_fk_currency_96170cc9 ON public.tasks USING btree (fk_currency);
CREATE INDEX tasks_fk_employee_1_c9b198a4 ON public.tasks USING btree (fk_employee_1);
CREATE INDEX tasks_fk_employee_2_1169876b ON public.tasks USING btree (fk_employee_2);
CREATE INDEX tasks_fk_invoice_ea3beb60 ON public.tasks USING btree (fk_invoice);
CREATE INDEX tasks_fk_project_fee5c3c8 ON public.tasks USING btree (fk_project);
CREATE INDEX tasks_fk_task_state_a8407fe2 ON public.tasks USING btree (fk_task_state);
CREATE INDEX tasks_fk_unit_acfa1ab8 ON public.tasks USING btree (fk_unit);
CREATE INDEX tasks_fk_vat_486022be ON public.tasks USING btree (fk_vat);


-- public.asset_absences definition

-- Drop table

-- DROP TABLE public.asset_absences;

CREATE TABLE public.asset_absences (
	id_asset_absence int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	asset_absence_date_from date NOT NULL,
	asset_absence_date_to date NOT NULL,
	fk_asset int4 NOT NULL,
	fk_asset_absence_code int4 NOT NULL,
	asset_absence_time_from time NOT NULL,
	asset_absence_time_to time NOT NULL,
	CONSTRAINT asset_absences_pkey PRIMARY KEY (id_asset_absence),
	CONSTRAINT asset_absences_fk_asset_9b20034e_fk_assets_id_asset FOREIGN KEY (fk_asset) REFERENCES public.assets(id_asset) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT asset_absences_fk_asset_absence_cod_83dd00a8_fk_asset_abs FOREIGN KEY (fk_asset_absence_code) REFERENCES public.asset_absence_codes(id_asset_absence_code) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX asset_absences_fk_asset_9b20034e ON public.asset_absences USING btree (fk_asset);
CREATE INDEX asset_absences_fk_asset_absence_code_83dd00a8 ON public.asset_absences USING btree (fk_asset_absence_code);