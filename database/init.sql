-- DROP SCHEMA public;



-- DROP SEQUENCE public.asset_absence_codes_id_asset_absence_code_seq;

CREATE SEQUENCE public.asset_absence_codes_id_asset_absence_code_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;



-- DROP SEQUENCE public.asset_absences_id_asset_absence_seq;

CREATE SEQUENCE public.asset_absences_id_asset_absence_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.asset_types_id_asset_type_seq;

CREATE SEQUENCE public.asset_types_id_asset_type_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.assets_id_asset_seq;

CREATE SEQUENCE public.assets_id_asset_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.auth_group_id_seq;

CREATE SEQUENCE public.auth_group_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.auth_group_permissions_id_seq;

CREATE SEQUENCE public.auth_group_permissions_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.auth_permission_id_seq;

CREATE SEQUENCE public.auth_permission_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.auth_user_groups_id_seq;

CREATE SEQUENCE public.auth_user_groups_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.auth_user_id_seq;

CREATE SEQUENCE public.auth_user_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.auth_user_user_permissions_id_seq;

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.companies_id_company_seq;

CREATE SEQUENCE public.companies_id_company_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.countries_id_country_seq;

CREATE SEQUENCE public.countries_id_country_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.currencies_id_currency_seq;

CREATE SEQUENCE public.currencies_id_currency_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.django_admin_log_id_seq;

CREATE SEQUENCE public.django_admin_log_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.django_content_type_id_seq;

CREATE SEQUENCE public.django_content_type_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.django_migrations_id_seq;

CREATE SEQUENCE public.django_migrations_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.employee_absence_codes_id_employee_absence_code_seq;

CREATE SEQUENCE public.employee_absence_codes_id_employee_absence_code_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.employee_absences_id_employee_absence_seq;

CREATE SEQUENCE public.employee_absences_id_employee_absence_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.employee_types_id_employee_type_seq;

CREATE SEQUENCE public.employee_types_id_employee_type_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.employees_id_employee_seq;

CREATE SEQUENCE public.employees_id_employee_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.invoice_states_id_invoice_state_seq;

CREATE SEQUENCE public.invoice_states_id_invoice_state_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.invoice_terms_id_invoice_term_seq;

CREATE SEQUENCE public.invoice_terms_id_invoice_term_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.invoice_texts_id_invoice_text_seq;

CREATE SEQUENCE public.invoice_texts_id_invoice_text_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.invoices_id_invoice_seq;

CREATE SEQUENCE public.invoices_id_invoice_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.projects_id_project_seq;

CREATE SEQUENCE public.projects_id_project_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.sales_id_sale_seq;

CREATE SEQUENCE public.sales_id_sale_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.sales_state_id_sales_state_seq;

CREATE SEQUENCE public.sales_state_id_sales_state_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.sys_rec_states_id_sys_rec_status_seq;

CREATE SEQUENCE public.sys_rec_states_id_sys_rec_status_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.task_states_id_task_state_seq;

CREATE SEQUENCE public.task_states_id_task_state_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.task_templates_id_task_template_seq;

CREATE SEQUENCE public.task_templates_id_task_template_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.tasks_id_task_seq;

CREATE SEQUENCE public.tasks_id_task_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.units_id_unit_seq;

CREATE SEQUENCE public.units_id_unit_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.vat_id_vat_seq;

CREATE SEQUENCE public.vat_id_vat_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;-- public.asset_absence_codes definition

-- Drop table

-- DROP TABLE public.asset_absence_codes;

CREATE TABLE public.asset_absence_codes (
	id_asset_absence_code int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	asset_absence_code varchar NOT NULL,
	asset_absence_code_abbreviation varchar NOT NULL,
	CONSTRAINT asset_absence_codes_pkey PRIMARY KEY (id_asset_absence_code)
);

COPY public.asset_absence_codes
FROM '/docker-entrypoint-initdb.d/asset_absence_codes.csv'
DELIMITER ','
CSV HEADER;

-- public.asset_types definition

-- Drop table

-- DROP TABLE public.asset_types;

CREATE TABLE public.asset_types (
	id_asset_type int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	asset_type varchar NOT NULL,
	CONSTRAINT asset_types_pkey PRIMARY KEY (id_asset_type)
);

COPY public.asset_types
FROM '/docker-entrypoint-initdb.d/asset_types.csv'
DELIMITER ','
CSV HEADER;
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

COPY public.auth_user
FROM '/docker-entrypoint-initdb.d/auth_user.csv'
DELIMITER ','
CSV HEADER;
-- public.countries definition

-- Drop table

-- DROP TABLE public.countries;

CREATE TABLE public.countries (
	id_country serial4 NOT NULL,
	country varchar NOT NULL,
	country_code varchar(3) NOT NULL,
	CONSTRAINT countries_pk PRIMARY KEY (id_country),
	CONSTRAINT countries_un UNIQUE (country)
);

COPY public.countries
FROM '/docker-entrypoint-initdb.d/countries.csv'
DELIMITER ','
CSV HEADER;

-- public.currencies definition

-- Drop table

-- DROP TABLE public.currencies;

CREATE TABLE public.currencies (
	id_currency int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	currency varchar NOT NULL,
	currency_abbreviation varchar NOT NULL,
	currency_account_nr varchar NOT NULL,
	CONSTRAINT currencies_pkey PRIMARY KEY (id_currency)
);

COPY public.currencies
FROM '/docker-entrypoint-initdb.d/currencies.csv'
DELIMITER ','
CSV HEADER;
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

COPY public.django_content_type
FROM '/docker-entrypoint-initdb.d/django_content_type.csv'
DELIMITER ','
CSV HEADER;
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
	employee_absence_code varchar NOT NULL,
	employee_absence_code_abbreviation varchar NOT NULL,
	CONSTRAINT employee_absence_codes_pkey PRIMARY KEY (id_employee_absence_code)
);

COPY public.employee_absence_codes
FROM '/docker-entrypoint-initdb.d/employee_absence_codes.csv'
DELIMITER ','
CSV HEADER;
-- public.django_

-- public.employee_types definition

-- Drop table

-- DROP TABLE public.employee_types;

CREATE TABLE public.employee_types (
	id_employee_type int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	employee_type_description varchar NOT NULL,
	CONSTRAINT employee_types_pkey PRIMARY KEY (id_employee_type)
);


COPY public.employee_types
FROM '/docker-entrypoint-initdb.d/employee_types.csv'
DELIMITER ','
CSV HEADER;
-- public.invoice_states definition

-- Drop table

-- DROP TABLE public.invoice_states;

CREATE TABLE public.invoice_states (
	id_invoice_state int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	invoice_state varchar NOT NULL,
	CONSTRAINT invoice_states_pkey PRIMARY KEY (id_invoice_state)
);

COPY public.invoice_states
FROM '/docker-entrypoint-initdb.d/invoice_states.csv'
DELIMITER ','
CSV HEADER;
-- public.invoice_terms definition

-- Drop table

-- DROP TABLE public.invoice_terms;

CREATE TABLE public.invoice_terms (
	id_invoice_term int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	due_days int4 NOT NULL,
	term_title varchar NOT NULL,
	CONSTRAINT invoice_terms_due_days_key UNIQUE (due_days),
	CONSTRAINT invoice_terms_pkey PRIMARY KEY (id_invoice_term)
);

COPY public.invoice_terms
FROM '/docker-entrypoint-initdb.d/invoice_terms.csv'
DELIMITER ','
CSV HEADER;
-- public.sales_state definition

-- Drop table

-- DROP TABLE public.sales_state;

CREATE TABLE public.sales_state (
	id_sales_state int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	sales_state varchar NOT NULL,
	CONSTRAINT sales_state_pkey PRIMARY KEY (id_sales_state),
	CONSTRAINT sales_state_sales_state_key UNIQUE (sales_state)
);
CREATE INDEX sales_state_sales_state_a193d641_like ON public.sales_state USING btree (sales_state varchar_pattern_ops);

COPY public.sales_state
FROM '/docker-entrypoint-initdb.d/sales_state.csv'
DELIMITER ','
CSV HEADER;
-- public.sys_rec_states definition

-- Drop table

-- DROP TABLE public.sys_rec_states;

CREATE TABLE public.sys_rec_states (
	id_sys_rec_status int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	sys_rec_status varchar NOT NULL,
	entity varchar NULL,
	CONSTRAINT sys_rec_states_pkey PRIMARY KEY (id_sys_rec_status)
);

COPY public.sys_rec_states
FROM '/docker-entrypoint-initdb.d/sys_rec_states.csv'
DELIMITER ','
CSV HEADER;
-- public.task_states definition

-- Drop table

-- DROP TABLE public.task_states;

CREATE TABLE public.task_states (
	id_task_state int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	task_state varchar NOT NULL,
	CONSTRAINT task_states_pkey PRIMARY KEY (id_task_state)
);

COPY public.task_states
FROM '/docker-entrypoint-initdb.d/task_states.csv'
DELIMITER ','
CSV HEADER;
-- public.units definition

-- Drop table

-- DROP TABLE public.units;

CREATE TABLE public.units (
	id_unit int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	unit varchar NOT NULL,
	unit_abbreviation varchar NOT NULL,
	CONSTRAINT units_pkey PRIMARY KEY (id_unit)
);

COPY public.units
FROM '/docker-entrypoint-initdb.d/units.csv'
DELIMITER ','
CSV HEADER;
-- public.vat definition

-- Drop table

-- DROP TABLE public.vat;

CREATE TABLE public.vat (
	id_vat int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	vat numeric(3, 3) NOT NULL,
	vat_title varchar NOT NULL,
	CONSTRAINT vat_pkey PRIMARY KEY (id_vat),
	CONSTRAINT vat_vat_key UNIQUE (vat)
);

COPY public.vat
FROM '/docker-entrypoint-initdb.d/vat.csv'
DELIMITER ','
CSV HEADER;
-- public.assets definition

-- Drop table

-- DROP TABLE public.assets;

CREATE TABLE public.assets (
	id_asset int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	asset_description varchar NOT NULL,
	asset_internal_alias varchar NOT NULL,
	year_of_production int4 NULL,
	fk_asset_type int4 NOT NULL,
	fk_sys_rec_status int4 NOT NULL,
	CONSTRAINT assets_pkey PRIMARY KEY (id_asset),
	CONSTRAINT assets_fk_asset_type_88e64c56_fk_asset_types_id_asset_type FOREIGN KEY (fk_asset_type) REFERENCES public.asset_types(id_asset_type) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT assets_fk_sys_rec_status_9f557fd4_fk_sys_rec_s FOREIGN KEY (fk_sys_rec_status) REFERENCES public.sys_rec_states(id_sys_rec_status) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX assets_fk_asset_type_88e64c56 ON public.assets USING btree (fk_asset_type);
CREATE INDEX assets_fk_sys_rec_status_9f557fd4 ON public.assets USING btree (fk_sys_rec_status);


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

COPY public.auth_permission
FROM '/docker-entrypoint-initdb.d/auth_permission.csv'
DELIMITER ','
CSV HEADER;
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


-- public.companies definition

-- Drop table

-- DROP TABLE public.companies;

CREATE TABLE public.companies (
	id_company int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	company_name varchar NOT NULL,
	company_street varchar NOT NULL,
	company_zipcode varchar NOT NULL,
	fk_country int4 NOT NULL,
	company_city varchar NOT NULL,
	company_internal_alias varchar NOT NULL,
	company_email varchar NULL,
	is_customer bool NULL,
	is_supplier bool NULL,
	is_subcontractor bool NULL,
	fk_sys_rec_status int4 NOT NULL,
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
	employee_first_name varchar NOT NULL,
	employee_last_name varchar NOT NULL,
	employee_street varchar NOT NULL,
	employee_zipcode varchar NOT NULL,
	employee_city varchar NOT NULL,
	employee_email varchar NOT NULL,
	employee_cell_phone varchar NOT NULL,
	employee_birthday date NOT NULL,
	employee_salary numeric(11, 2) NULL,
	employee_fte numeric(3, 2) NULL,
	employee_internal_alias varchar NOT NULL,
	fk_employee_type int4 NOT NULL,
	fk_sys_rec_status int4 NOT NULL,
	fk_country int4 NOT NULL,
	CONSTRAINT employees_employee_internal_alias_key UNIQUE (employee_internal_alias),
	CONSTRAINT employees_pkey PRIMARY KEY (id_employee),
	CONSTRAINT employees_fk FOREIGN KEY (fk_country) REFERENCES public.countries(id_country),
	CONSTRAINT employees_fk_employee_type_236e57e4_fk_employee_ FOREIGN KEY (fk_employee_type) REFERENCES public.employee_types(id_employee_type) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT employees_fk_sys_rec_status_f319e4a4_fk_sys_rec_s FOREIGN KEY (fk_sys_rec_status) REFERENCES public.sys_rec_states(id_sys_rec_status) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX employees_employee_internal_alias_5fdb54d3_like ON public.employees USING btree (employee_internal_alias varchar_pattern_ops);
CREATE INDEX employees_fk_employee_type_236e57e4 ON public.employees USING btree (fk_employee_type);
CREATE INDEX employees_fk_sys_rec_status_f319e4a4 ON public.employees USING btree (fk_sys_rec_status);


-- public.invoice_texts definition

-- Drop table

-- DROP TABLE public.invoice_texts;

CREATE TABLE public.invoice_texts (
	id_invoice_text int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	invoice_text varchar NOT NULL,
	fk_customer int4 NOT NULL,
	CONSTRAINT invoice_texts_pkey PRIMARY KEY (id_invoice_text),
	CONSTRAINT invoice_texts_fk_customer_765c2502_fk_companies_id_company FOREIGN KEY (fk_customer) REFERENCES public.companies(id_company) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX invoice_texts_fk_customer_765c2502 ON public.invoice_texts USING btree (fk_customer);


-- public.invoices definition

-- Drop table

-- DROP TABLE public.invoices;

CREATE TABLE public.invoices (
	id_invoice int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	invoice_date date NOT NULL,
	invoice_text varchar NULL,
	fk_invoice_state int4 NOT NULL,
	fk_invoice_terms int4 NOT NULL,
	CONSTRAINT invoices_pkey PRIMARY KEY (id_invoice),
	CONSTRAINT invoices_fk_invoice_state_e9e847ba_fk_invoice_s FOREIGN KEY (fk_invoice_state) REFERENCES public.invoice_states(id_invoice_state) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT invoices_fk_invoice_terms_3036695b_fk_invoice_t FOREIGN KEY (fk_invoice_terms) REFERENCES public.invoice_terms(id_invoice_term) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX invoices_fk_invoice_state_e9e847ba ON public.invoices USING btree (fk_invoice_state);
CREATE INDEX invoices_fk_invoice_terms_3036695b ON public.invoices USING btree (fk_invoice_terms);


-- public.projects definition

-- Drop table

-- DROP TABLE public.projects;

CREATE TABLE public.projects (
	id_project int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	project_name varchar NOT NULL,
	start_date date NOT NULL,
	end_date date NOT NULL,
	fk_customer int4 NOT NULL,
	fk_sys_rec_status int4 NOT NULL,
	CONSTRAINT projects_pkey PRIMARY KEY (id_project),
	CONSTRAINT projects_fk FOREIGN KEY (fk_sys_rec_status) REFERENCES public.sys_rec_states(id_sys_rec_status),
	CONSTRAINT projects_fk_customer_32d0f6c7_fk_companies_id_company FOREIGN KEY (fk_customer) REFERENCES public.companies(id_company) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX projects_fk_customer_32d0f6c7 ON public.projects USING btree (fk_customer);


-- public.sales definition

-- Drop table

-- DROP TABLE public.sales;

CREATE TABLE public.sales (
	id_sale int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	sale_date date NOT NULL,
	sale_amount numeric(11, 2) NOT NULL,
	sale_unit_price numeric(11, 2) NOT NULL,
	sale_reference varchar NOT NULL,
	sale_description varchar NULL,
	sale_time time NULL,
	fk_currency int4 NULL,
	fk_invoice int4 NULL,
	fk_project int4 NOT NULL,
	fk_sales_status int4 NULL,
	fk_unit int4 NOT NULL,
	fk_vat int4 NULL,
	CONSTRAINT sales_pkey PRIMARY KEY (id_sale),
	CONSTRAINT sales_fk_currency_43dcbc47_fk_currencies_id_currency FOREIGN KEY (fk_currency) REFERENCES public.currencies(id_currency) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT sales_fk_invoice_0a9cd917_fk_invoices_id_invoice FOREIGN KEY (fk_invoice) REFERENCES public.invoices(id_invoice) DEFERRABLE INITIALLY DEFERRED,
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


-- public.task_templates definition

-- Drop table

-- DROP TABLE public.task_templates;

CREATE TABLE public.task_templates (
	id_task_template int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	fk_project int4 NULL,
	amount numeric(11, 2) NOT NULL,
	unit_price numeric(11, 2) NOT NULL,
	task_description varchar NOT NULL,
	fk_currency int4 NULL,
	fk_unit int4 NOT NULL,
	fk_vat int4 NULL,
	CONSTRAINT task_templates_pkey PRIMARY KEY (id_task_template),
	CONSTRAINT task_templates_fk_currency_315f0c49_fk_currencies_id_currency FOREIGN KEY (fk_currency) REFERENCES public.currencies(id_currency) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT task_templates_fk_unit_69400482_fk_units_id_unit FOREIGN KEY (fk_unit) REFERENCES public.units(id_unit) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT task_templates_fk_vat_12a8af6b_fk_vat_id_vat FOREIGN KEY (fk_vat) REFERENCES public.vat(id_vat) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX task_templates_fk_currency_315f0c49 ON public.task_templates USING btree (fk_currency);
CREATE INDEX task_templates_fk_unit_69400482 ON public.task_templates USING btree (fk_unit);
CREATE INDEX task_templates_fk_vat_12a8af6b ON public.task_templates USING btree (fk_vat);


-- public.tasks definition

-- Drop table

-- DROP TABLE public.tasks;

CREATE TABLE public.tasks (
	id_task int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	task_date_from date NULL,
	task_date_to date NULL,
	amount numeric(11, 2) NULL,
	unit_price numeric(11, 2) NULL,
	task_description varchar NOT NULL,
	internal_info varchar NULL,
	customer_reference varchar NULL,
	fk_subcontractor int4 NULL,
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
	CONSTRAINT tasks_pkey PRIMARY KEY (id_task),
	CONSTRAINT tasks_fk_asset_1_477b32a9_fk_assets_id_asset FOREIGN KEY (fk_asset_1) REFERENCES public.assets(id_asset) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_asset_2_96e85ef9_fk_assets_id_asset FOREIGN KEY (fk_asset_2) REFERENCES public.assets(id_asset) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_currency_96170cc9_fk_currencies_id_currency FOREIGN KEY (fk_currency) REFERENCES public.currencies(id_currency) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_employee_1_c9b198a4_fk_employees_id_employee FOREIGN KEY (fk_employee_1) REFERENCES public.employees(id_employee) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_employee_2_1169876b_fk_employees_id_employee FOREIGN KEY (fk_employee_2) REFERENCES public.employees(id_employee) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT tasks_fk_invoice_ea3beb60_fk_invoices_id_invoice FOREIGN KEY (fk_invoice) REFERENCES public.invoices(id_invoice) DEFERRABLE INITIALLY DEFERRED,
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
	asset_absence_from timestamptz NOT NULL,
	asset_absence_to timestamptz NOT NULL,
	fk_asset int4 NOT NULL,
	fk_asset_absence_code int4 NOT NULL,
	CONSTRAINT asset_absences_pkey PRIMARY KEY (id_asset_absence),
	CONSTRAINT asset_absences_fk_asset_9b20034e_fk_assets_id_asset FOREIGN KEY (fk_asset) REFERENCES public.assets(id_asset) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT asset_absences_fk_asset_absence_cod_83dd00a8_fk_asset_abs FOREIGN KEY (fk_asset_absence_code) REFERENCES public.asset_absence_codes(id_asset_absence_code) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX asset_absences_fk_asset_9b20034e ON public.asset_absences USING btree (fk_asset);
CREATE INDEX asset_absences_fk_asset_absence_code_83dd00a8 ON public.asset_absences USING btree (fk_asset_absence_code);


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


-- public.employee_absences definition

-- Drop table

-- DROP TABLE public.employee_absences;

CREATE TABLE public.employee_absences (
	id_employee_absence int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	employee_absence_from timestamptz NOT NULL,
	employee_absence_to timestamptz NOT NULL,
	fk_employee int4 NOT NULL,
	fk_employee_absence_code int4 NOT NULL,
	CONSTRAINT employee_absences_pkey PRIMARY KEY (id_employee_absence),
	CONSTRAINT employee_absences_fk_employee_absence__0f106f50_fk_employee_ FOREIGN KEY (fk_employee_absence_code) REFERENCES public.employee_absence_codes(id_employee_absence_code) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT employee_absences_fk_employee_d330c4d2_fk_employees_id_employee FOREIGN KEY (fk_employee) REFERENCES public.employees(id_employee) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX employee_absences_fk_employee_absence_code_0f106f50 ON public.employee_absences USING btree (fk_employee_absence_code);
CREATE INDEX employee_absences_fk_employee_d330c4d2 ON public.employee_absences USING btree (fk_employee);
