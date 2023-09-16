-- DROP SCHEMA public;


-- DROP SEQUENCE public.asset_types_id_asset_type_seq;

CREATE SEQUENCE public.asset_types_id_asset_type_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.asset_types_id_asset_type_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.asset_types_id_asset_type_seq TO hello_django;

-- DROP SEQUENCE public.assets_id_asset_seq;

CREATE SEQUENCE public.assets_id_asset_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.assets_id_asset_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.assets_id_asset_seq TO hello_django;

-- DROP SEQUENCE public.auth_group_id_seq;

CREATE SEQUENCE public.auth_group_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.auth_group_id_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.auth_group_id_seq TO hello_django;

-- DROP SEQUENCE public.auth_group_permissions_id_seq;

CREATE SEQUENCE public.auth_group_permissions_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.auth_group_permissions_id_seq TO hello_django;

-- DROP SEQUENCE public.auth_permission_id_seq;

CREATE SEQUENCE public.auth_permission_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.auth_permission_id_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.auth_permission_id_seq TO hello_django;

-- DROP SEQUENCE public.auth_user_groups_id_seq;

CREATE SEQUENCE public.auth_user_groups_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.auth_user_groups_id_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.auth_user_groups_id_seq TO hello_django;

-- DROP SEQUENCE public.auth_user_id_seq;

CREATE SEQUENCE public.auth_user_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.auth_user_id_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.auth_user_id_seq TO hello_django;

-- DROP SEQUENCE public.auth_user_user_permissions_id_seq;

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.auth_user_user_permissions_id_seq TO hello_django;

-- DROP SEQUENCE public.curency_id_currency_seq;

CREATE SEQUENCE public.curency_id_currency_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.curency_id_currency_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.curency_id_currency_seq TO hello_django;

-- DROP SEQUENCE public.customer_invoice_text_id_customer_invoice_text_seq;

CREATE SEQUENCE public.customer_invoice_text_id_customer_invoice_text_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.customer_invoice_text_id_customer_invoice_text_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.customer_invoice_text_id_customer_invoice_text_seq TO hello_django;

-- DROP SEQUENCE public.django_admin_log_id_seq;

CREATE SEQUENCE public.django_admin_log_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.django_admin_log_id_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.django_admin_log_id_seq TO hello_django;

-- DROP SEQUENCE public.django_content_type_id_seq;

CREATE SEQUENCE public.django_content_type_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.django_content_type_id_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.django_content_type_id_seq TO hello_django;

-- DROP SEQUENCE public.django_migrations_id_seq;

CREATE SEQUENCE public.django_migrations_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.django_migrations_id_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.django_migrations_id_seq TO hello_django;

-- DROP SEQUENCE public.employee_absence_code_id_employee_absence_code_seq;

CREATE SEQUENCE public.employee_absence_code_id_employee_absence_code_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.employee_absence_code_id_employee_absence_code_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.employee_absence_code_id_employee_absence_code_seq TO hello_django;

-- DROP SEQUENCE public.employee_absence_id_employee_absence_seq;

CREATE SEQUENCE public.employee_absence_id_employee_absence_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.employee_absence_id_employee_absence_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.employee_absence_id_employee_absence_seq TO hello_django;

-- DROP SEQUENCE public.employee_id_employee_seq;

CREATE SEQUENCE public.employee_id_employee_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.employee_id_employee_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.employee_id_employee_seq TO hello_django;

-- DROP SEQUENCE public.employee_type_employee_type_seq;

CREATE SEQUENCE public.employee_type_employee_type_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.employee_type_employee_type_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.employee_type_employee_type_seq TO hello_django;

-- DROP SEQUENCE public.invoice_id_invoice_seq;

CREATE SEQUENCE public.invoice_id_invoice_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.invoice_id_invoice_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.invoice_id_invoice_seq TO hello_django;

-- DROP SEQUENCE public.invoice_status_id_invoice_status_seq;

CREATE SEQUENCE public.invoice_status_id_invoice_status_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.invoice_status_id_invoice_status_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.invoice_status_id_invoice_status_seq TO hello_django;

-- DROP SEQUENCE public.newtable_id_customer_seq;

CREATE SEQUENCE public.newtable_id_customer_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.newtable_id_customer_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.newtable_id_customer_seq TO hello_django;

-- DROP SEQUENCE public.payment_conditions_id_payment_condition_seq;

CREATE SEQUENCE public.payment_conditions_id_payment_condition_seq
	NO MINVALUE
	NO MAXVALUE;

-- Permissions

ALTER SEQUENCE public.payment_conditions_id_payment_condition_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.payment_conditions_id_payment_condition_seq TO hello_django;

-- DROP SEQUENCE public.projects_id_project_seq;

CREATE SEQUENCE public.projects_id_project_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.projects_id_project_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.projects_id_project_seq TO hello_django;

-- DROP SEQUENCE public.sales_id_sale_seq;

CREATE SEQUENCE public.sales_id_sale_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.sales_id_sale_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.sales_id_sale_seq TO hello_django;

-- DROP SEQUENCE public.service_states_id_service_state_seq;

CREATE SEQUENCE public.service_states_id_service_state_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.service_states_id_service_state_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.service_states_id_service_state_seq TO hello_django;

-- DROP SEQUENCE public.service_templates_id_service_template_seq;

CREATE SEQUENCE public.service_templates_id_service_template_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.service_templates_id_service_template_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.service_templates_id_service_template_seq TO hello_django;

-- DROP SEQUENCE public.services_id_service_seq;

CREATE SEQUENCE public.services_id_service_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.services_id_service_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.services_id_service_seq TO hello_django;

-- DROP SEQUENCE public.sys_rec_states_id_sys_rec_status_seq;

CREATE SEQUENCE public.sys_rec_states_id_sys_rec_status_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.sys_rec_states_id_sys_rec_status_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.sys_rec_states_id_sys_rec_status_seq TO hello_django;

-- DROP SEQUENCE public.units_id_unit_seq;

CREATE SEQUENCE public.units_id_unit_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.units_id_unit_seq OWNER TO hello_django;
GRANT ALL ON SEQUENCE public.units_id_unit_seq TO hello_django;
-- public.asset_absence_codes definition

-- Drop table

-- DROP TABLE public.asset_absence_codes;

CREATE TABLE public.asset_absence_codes (
	id_asset_absence_code int4 NOT NULL DEFAULT nextval('employee_absence_code_id_employee_absence_code_seq'::regclass),
	asset_absence_code varchar NOT NULL,
	asset_absence_code_abbreviation varchar NOT NULL,
	CONSTRAINT asset_absence_code_pk PRIMARY KEY (id_asset_absence_code)
);

-- Permissions

ALTER TABLE public.asset_absence_codes OWNER TO hello_django;
GRANT ALL ON TABLE public.asset_absence_codes TO hello_django;


-- public.asset_types definition

-- Drop table

-- DROP TABLE public.asset_types;

CREATE TABLE public.asset_types (
	id_asset_type serial4 NOT NULL,
	asset_type varchar NOT NULL,
	max_capacity numeric NULL,
	CONSTRAINT asset_types_pk PRIMARY KEY (id_asset_type)
);

-- Permissions

ALTER TABLE public.asset_types OWNER TO hello_django;
GRANT ALL ON TABLE public.asset_types TO hello_django;


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

-- Permissions

ALTER TABLE public.auth_group OWNER TO hello_django;
GRANT ALL ON TABLE public.auth_group TO hello_django;


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

-- Permissions

ALTER TABLE public.auth_user OWNER TO hello_django;
GRANT ALL ON TABLE public.auth_user TO hello_django;


-- public.currencies definition

-- Drop table

-- DROP TABLE public.currencies;

CREATE TABLE public.currencies (
	id_currency int4 NOT NULL DEFAULT nextval('curency_id_currency_seq'::regclass),
	currency varchar NOT NULL,
	currency_abbreviation varchar NOT NULL,
	currency_account_nr varchar NOT NULL,
	CONSTRAINT curency_pk PRIMARY KEY (id_currency)
);

-- Permissions

ALTER TABLE public.currencies OWNER TO hello_django;
GRANT ALL ON TABLE public.currencies TO hello_django;


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

-- Permissions

ALTER TABLE public.django_content_type OWNER TO hello_django;
GRANT ALL ON TABLE public.django_content_type TO hello_django;


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

-- Permissions

ALTER TABLE public.django_migrations OWNER TO hello_django;
GRANT ALL ON TABLE public.django_migrations TO hello_django;


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

-- Permissions

ALTER TABLE public.django_session OWNER TO hello_django;
GRANT ALL ON TABLE public.django_session TO hello_django;


-- public.employee_absence_codes definition

-- Drop table

-- DROP TABLE public.employee_absence_codes;

CREATE TABLE public.employee_absence_codes (
	id_employee_absence_code int4 NOT NULL DEFAULT nextval('employee_absence_code_id_employee_absence_code_seq'::regclass),
	employee_absence_code varchar NOT NULL,
	employee_absence_code_abbreviation varchar NOT NULL,
	CONSTRAINT employee_absence_code_pk PRIMARY KEY (id_employee_absence_code)
);

-- Permissions

ALTER TABLE public.employee_absence_codes OWNER TO hello_django;
GRANT ALL ON TABLE public.employee_absence_codes TO hello_django;


-- public.employee_types definition

-- Drop table

-- DROP TABLE public.employee_types;

CREATE TABLE public.employee_types (
	id_employee_type int4 NOT NULL DEFAULT nextval('employee_type_employee_type_seq'::regclass),
	employee_type_description varchar NOT NULL,
	CONSTRAINT employee_type_pk PRIMARY KEY (id_employee_type)
);

-- Permissions

ALTER TABLE public.employee_types OWNER TO hello_django;
GRANT ALL ON TABLE public.employee_types TO hello_django;


-- public.invoice_states definition

-- Drop table

-- DROP TABLE public.invoice_states;

CREATE TABLE public.invoice_states (
	id_invoice_state int4 NOT NULL DEFAULT nextval('invoice_status_id_invoice_status_seq'::regclass),
	invoice_state varchar NOT NULL,
	invoice_state_abbreviation int4 NOT NULL,
	CONSTRAINT invoice_status_pk PRIMARY KEY (id_invoice_state)
);

-- Permissions

ALTER TABLE public.invoice_states OWNER TO hello_django;
GRANT ALL ON TABLE public.invoice_states TO hello_django;


-- public.sys_rec_states definition

-- Drop table

-- DROP TABLE public.sys_rec_states;

CREATE TABLE public.sys_rec_states (
	id_sys_rec_status serial4 NOT NULL,
	sys_rec_status varchar NOT NULL,
	entity varchar NULL,
	CONSTRAINT sys_rec_states_pk PRIMARY KEY (id_sys_rec_status)
);

-- Permissions

ALTER TABLE public.sys_rec_states OWNER TO hello_django;
GRANT ALL ON TABLE public.sys_rec_states TO hello_django;


-- public.task_states definition

-- Drop table

-- DROP TABLE public.task_states;

CREATE TABLE public.task_states (
	id_task_state int4 NOT NULL DEFAULT nextval('service_states_id_service_state_seq'::regclass),
	task_state varchar NOT NULL,
	CONSTRAINT service_states_pk PRIMARY KEY (id_task_state)
);

-- Permissions

ALTER TABLE public.task_states OWNER TO hello_django;
GRANT ALL ON TABLE public.task_states TO hello_django;


-- public.units definition

-- Drop table

-- DROP TABLE public.units;

CREATE TABLE public.units (
	id_unit serial4 NOT NULL,
	unit varchar NOT NULL,
	unit_abbreviation varchar NOT NULL,
	CONSTRAINT units_pk PRIMARY KEY (id_unit)
);

-- Permissions

ALTER TABLE public.units OWNER TO hello_django;
GRANT ALL ON TABLE public.units TO hello_django;


-- public.vat definition

-- Drop table

-- DROP TABLE public.vat;

CREATE TABLE public.vat (
	id_vat serial4 NOT NULL,
	vat numeric(3, 3) NOT NULL,
	vat_title varchar NOT NULL,
	CONSTRAINT vat_pk PRIMARY KEY (id_vat)
);

-- Permissions

ALTER TABLE public.vat OWNER TO hello_django;
GRANT ALL ON TABLE public.vat TO hello_django;


-- public.sales_state definition

-- Drop table

-- DROP TABLE public.sales_state;

CREATE TABLE public.sales_state (
	id_sales_state serial4 NOT NULL,
	sales_state varchar NOT NULL,
	CONSTRAINT sales_state_pk PRIMARY KEY (id_sales_state)
);

-- Permissions

ALTER TABLE public.sales_state OWNER TO hello_django;
GRANT ALL ON TABLE public.sales_state TO hello_django;


-- public.invoice_terms definition

-- Drop table

-- DROP TABLE public.invoice_terms;

CREATE TABLE public.invoice_terms (
	id_invoice_term serial4 NOT NULL,
	due_days int4 NOT NULL,
	term_title varchar NOT NULL,
	CONSTRAINT invoice_terms_pk PRIMARY KEY (id_invoice_term)
);

-- Permissions

ALTER TABLE public.invoice_terms OWNER TO hello_django;
GRANT ALL ON TABLE public.invoice_terms TO hello_django;


-- public.assets definition

-- Drop table

-- DROP TABLE public.assets;

CREATE TABLE public.assets (
	id_asset serial4 NOT NULL,
	fk_asset_type int4 NOT NULL,
	asset_description varchar NOT NULL,
	asset_internal_alias varchar NOT NULL,
	year_of_production int4 NULL,
	fk_sys_rec_status int4 NOT NULL,
	CONSTRAINT assets_pk PRIMARY KEY (id_asset),
	CONSTRAINT assets_fk FOREIGN KEY (fk_asset_type) REFERENCES public.asset_types(id_asset_type),
	CONSTRAINT assets_rec_status FOREIGN KEY (fk_sys_rec_status) REFERENCES public.sys_rec_states(id_sys_rec_status)
);

-- Permissions

ALTER TABLE public.assets OWNER TO hello_django;
GRANT ALL ON TABLE public.assets TO hello_django;


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

-- Permissions

ALTER TABLE public.auth_permission OWNER TO hello_django;
GRANT ALL ON TABLE public.auth_permission TO hello_django;


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

-- Permissions

ALTER TABLE public.auth_user_groups OWNER TO hello_django;
GRANT ALL ON TABLE public.auth_user_groups TO hello_django;


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

-- Permissions

ALTER TABLE public.auth_user_user_permissions OWNER TO hello_django;
GRANT ALL ON TABLE public.auth_user_user_permissions TO hello_django;


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

-- Permissions

ALTER TABLE public.authtoken_token OWNER TO hello_django;
GRANT ALL ON TABLE public.authtoken_token TO hello_django;


-- public.companies definition

-- Drop table

-- DROP TABLE public.companies;

CREATE TABLE public.companies (
	id_company int4 NOT NULL DEFAULT nextval('newtable_id_customer_seq'::regclass),
	company_name varchar NOT NULL,
	company_street varchar NOT NULL,
	company_zipcode varchar NOT NULL,
	company_country varchar NOT NULL,
	company_city varchar NOT NULL,
	company_internal_alias varchar NOT NULL,
	fk_sys_rec_status int4 NOT NULL,
	company_email varchar NULL,
	is_customer bool NULL,
	is_supplier bool NULL,
	is_subcontractor bool NULL,
	CONSTRAINT newtable_pk PRIMARY KEY (id_company),
	CONSTRAINT newtable_un UNIQUE (company_internal_alias),
	CONSTRAINT companies_fk FOREIGN KEY (fk_sys_rec_status) REFERENCES public.sys_rec_states(id_sys_rec_status)
);



-- Permissions

ALTER TABLE public.companies OWNER TO hello_django;
GRANT ALL ON TABLE public.companies TO hello_django;


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

-- Permissions

ALTER TABLE public.django_admin_log OWNER TO hello_django;
GRANT ALL ON TABLE public.django_admin_log TO hello_django;


-- public.employees definition

-- Drop table

-- DROP TABLE public.employees;

CREATE TABLE public.employees (
	id_employee int4 NOT NULL DEFAULT nextval('employee_id_employee_seq'::regclass),
	employee_first_name varchar NOT NULL,
	employee_last_name varchar NOT NULL,
	employee_street varchar NOT NULL,
	employee_zipcode varchar NOT NULL,
	employee_city varchar NOT NULL,
	employee_email varchar NOT NULL,
	employee_cell_phone varchar NOT NULL,
	employee_birthday date NOT NULL,
	employee_salary numeric NULL,
	fk_employee_type int4 NOT NULL,
	employee_fte numeric NULL DEFAULT 1,
	employee_internal_alias varchar NOT NULL,
	fk_sys_rec_status int4 NOT NULL,
	CONSTRAINT employee_pk PRIMARY KEY (id_employee),
	CONSTRAINT employee_un UNIQUE (employee_internal_alias),
	CONSTRAINT employees_fk FOREIGN KEY (fk_sys_rec_status) REFERENCES public.sys_rec_states(id_sys_rec_status),
	CONSTRAINT fk_employee_type FOREIGN KEY (fk_employee_type) REFERENCES public.employee_types(id_employee_type)
);

-- Permissions

ALTER TABLE public.employees OWNER TO hello_django;
GRANT ALL ON TABLE public.employees TO hello_django;


-- public.invoice_texts definition

-- Drop table

-- DROP TABLE public.invoice_texts;

CREATE TABLE public.invoice_texts (
	id_invoice_text int4 NOT NULL DEFAULT nextval('customer_invoice_text_id_customer_invoice_text_seq'::regclass),
	invoice_text varchar NOT NULL,
	fk_customer int4 NOT NULL,
	CONSTRAINT customer_invoice_text_pk PRIMARY KEY (id_invoice_text),
	CONSTRAINT customer_invoice_text_fk FOREIGN KEY (fk_customer) REFERENCES public.companies(id_company)
);

-- Permissions

ALTER TABLE public.invoice_texts OWNER TO hello_django;
GRANT ALL ON TABLE public.invoice_texts TO hello_django;


-- public.invoices definition

-- Drop table

-- DROP TABLE public.invoices;

CREATE TABLE public.invoices (
	id_invoice int4 NOT NULL DEFAULT nextval('invoice_id_invoice_seq'::regclass),
	invoice_date date NULL,
	invoice_text varchar NULL,
	fk_invoice_state int4 NOT NULL,
	fk_invoice_terms int4 NOT NULL,
	CONSTRAINT invoices_pk PRIMARY KEY (id_invoice),
	CONSTRAINT invoices_fk FOREIGN KEY (fk_invoice_terms) REFERENCES public.invoice_terms(id_invoice_term),
	CONSTRAINT invoices_fk_2 FOREIGN KEY (fk_invoice_state) REFERENCES public.invoice_states(id_invoice_state)
);

-- Permissions

ALTER TABLE public.invoices OWNER TO hello_django;
GRANT ALL ON TABLE public.invoices TO hello_django;


-- public.projects definition

-- Drop table

-- DROP TABLE public.projects;

CREATE TABLE public.projects (
	id_project serial4 NOT NULL,
	project_name varchar NOT NULL,
	fk_customer int4 NOT NULL,
	planned_start_date date NOT NULL,
	planned_end_date date NOT NULL,
	effective_start_date date NULL,
	effective_end_date date NULL,
	CONSTRAINT projects_pk PRIMARY KEY (id_project),
	CONSTRAINT projects_fk FOREIGN KEY (fk_customer) REFERENCES public.companies(id_company)
);

-- Permissions

ALTER TABLE public.projects OWNER TO hello_django;
GRANT ALL ON TABLE public.projects TO hello_django;


-- public.sales definition

-- Drop table

-- DROP TABLE public.sales;

CREATE TABLE public.sales (
	id_sale serial4 NOT NULL,
	sale_date timestamp NOT NULL,
	fk_project int4 NOT NULL,
	sale_amount numeric(11, 2) NOT NULL,
	sale_unit_price numeric(11, 2) NOT NULL,
	sale_reference varchar NOT NULL,
	fk_unit int4 NOT NULL,
	fk_invoice int4 NULL,
	sale_description varchar NULL,
	sale_time time NULL,
	fk_vat int4 NULL,
	fk_sales_status int4 NULL,
	fk_currency int4 NULL,
	CONSTRAINT sales_pk PRIMARY KEY (id_sale),
	CONSTRAINT sales_fk FOREIGN KEY (fk_project) REFERENCES public.projects(id_project),
	CONSTRAINT sales_fk3 FOREIGN KEY (fk_invoice) REFERENCES public.invoices(id_invoice),
	CONSTRAINT sales_fk_2 FOREIGN KEY (fk_unit) REFERENCES public.units(id_unit),
	CONSTRAINT sales_fk_currency FOREIGN KEY (fk_currency) REFERENCES public.currencies(id_currency),
	CONSTRAINT sales_fk_state FOREIGN KEY (fk_sales_status) REFERENCES public.sales_state(id_sales_state),
	CONSTRAINT sales_fk_vat FOREIGN KEY (fk_vat) REFERENCES public.vat(id_vat)
);

-- Permissions

ALTER TABLE public.sales OWNER TO hello_django;
GRANT ALL ON TABLE public.sales TO hello_django;


-- public.task_templates definition

-- Drop table

-- DROP TABLE public.task_templates;

CREATE TABLE public.task_templates (
	id_task_template int4 NOT NULL DEFAULT nextval('service_templates_id_service_template_seq'::regclass),
	fk_project int4 NOT NULL,
	fk_unit int4 NOT NULL,
	amount numeric NOT NULL,
	unit_price numeric NOT NULL,
	task_description varchar NOT NULL,
	fk_currency int4 NULL,
	fk_vat int4 NULL,
	CONSTRAINT service_templates_pk PRIMARY KEY (id_task_template),
	CONSTRAINT service_templates_fk_1 FOREIGN KEY (fk_unit) REFERENCES public.units(id_unit),
	CONSTRAINT task_templates_fk FOREIGN KEY (fk_vat) REFERENCES public.vat(id_vat),
	CONSTRAINT task_templates_fk_1 FOREIGN KEY (fk_currency) REFERENCES public.currencies(id_currency),
	CONSTRAINT task_templates_fk_proj FOREIGN KEY (fk_project) REFERENCES public.projects(id_project)
);

-- Permissions

ALTER TABLE public.task_templates OWNER TO hello_django;
GRANT ALL ON TABLE public.task_templates TO hello_django;


-- public.tasks definition

-- Drop table

-- DROP TABLE public.tasks;

CREATE TABLE public.tasks (
	id_task int4 NOT NULL DEFAULT nextval('services_id_service_seq'::regclass),
	fk_project int4 NOT NULL,
	fk_task_state int4 NOT NULL,
	task_date_from date NULL,
	task_date_to date NULL,
	amount numeric(11, 2) NULL,
	unit_price numeric(11, 2) NULL,
	task_description varchar NOT NULL,
	fk_invoice int4 NULL,
	fk_unit int4 NULL,
	internal_info varchar NULL,
	customer_reference varchar NULL,
	fk_subcontractor int4 NULL,
	fk_employee_1 int4 NULL,
	fk_employee_2 int4 NULL,
	fk_asset_1 int4 NULL,
	fk_asset_2 int4 NULL,
	task_time_from time NULL,
	task_time_to time NULL,
	fk_currency int4 NULL,
	fk_vat int4 NULL,
	CONSTRAINT services_pk PRIMARY KEY (id_task),
	CONSTRAINT fk_asset_1 FOREIGN KEY (fk_asset_1) REFERENCES public.assets(id_asset),
	CONSTRAINT fk_asset_2 FOREIGN KEY (fk_asset_2) REFERENCES public.assets(id_asset),
	CONSTRAINT fk_employee_1 FOREIGN KEY (fk_employee_1) REFERENCES public.employees(id_employee),
	CONSTRAINT fk_employee_2 FOREIGN KEY (fk_employee_2) REFERENCES public.employees(id_employee),
	CONSTRAINT service_state FOREIGN KEY (fk_task_state) REFERENCES public.task_states(id_task_state),
	CONSTRAINT services_fk FOREIGN KEY (fk_unit) REFERENCES public.units(id_unit),
	CONSTRAINT services_fk3 FOREIGN KEY (fk_invoice) REFERENCES public.invoices(id_invoice),
	CONSTRAINT tasks_fk FOREIGN KEY (fk_project) REFERENCES public.projects(id_project),
	CONSTRAINT tasks_fk_currency FOREIGN KEY (fk_currency) REFERENCES public.currencies(id_currency),
	CONSTRAINT tasks_fk_vat FOREIGN KEY (fk_vat) REFERENCES public.vat(id_vat)
);

-- Permissions

ALTER TABLE public.tasks OWNER TO hello_django;
GRANT ALL ON TABLE public.tasks TO hello_django;


-- public.asset_absences definition

-- Drop table

-- DROP TABLE public.asset_absences;

CREATE TABLE public.asset_absences (
	id_asset_absence int4 NOT NULL DEFAULT nextval('employee_absence_id_employee_absence_seq'::regclass),
	asset_absence_from timestamp NOT NULL,
	asset_absence_to timestamp NOT NULL,
	fk_asset int4 NOT NULL,
	fk_asset_absence_code int4 NOT NULL,
	CONSTRAINT asset_absences_pk PRIMARY KEY (id_asset_absence),
	CONSTRAINT asset_absences_fk FOREIGN KEY (fk_asset_absence_code) REFERENCES public.asset_absence_codes(id_asset_absence_code),
	CONSTRAINT asset_absences_fk_1 FOREIGN KEY (fk_asset) REFERENCES public.assets(id_asset)
);

-- Permissions

ALTER TABLE public.asset_absences OWNER TO hello_django;
GRANT ALL ON TABLE public.asset_absences TO hello_django;


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

-- Permissions

ALTER TABLE public.auth_group_permissions OWNER TO hello_django;
GRANT ALL ON TABLE public.auth_group_permissions TO hello_django;


-- public.employee_absences definition

-- Drop table

-- DROP TABLE public.employee_absences;

CREATE TABLE public.employee_absences (
	id_employee_absence int4 NOT NULL DEFAULT nextval('employee_absence_id_employee_absence_seq'::regclass),
	employee_absence_from timestamp NOT NULL,
	employee_absence_to timestamp NOT NULL,
	fk_employee int4 NOT NULL,
	fk_employee_absence_code int4 NOT NULL,
	CONSTRAINT employee_absences_pk PRIMARY KEY (id_employee_absence),
	CONSTRAINT employee_absence_fk FOREIGN KEY (fk_employee_absence_code) REFERENCES public.employee_absence_codes(id_employee_absence_code),
	CONSTRAINT employee_absence_fk_1 FOREIGN KEY (fk_employee) REFERENCES public.employees(id_employee)
);

-- Permissions

ALTER TABLE public.employee_absences OWNER TO hello_django;
GRANT ALL ON TABLE public.employee_absences TO hello_django;



CREATE OR REPLACE FUNCTION public.f_create_default_project()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
declare default_cnt integer;
begin
	SELECT count(*) INTO default_cnt FROM public.projects WHERE project_name = CONCAT(new.company_name, '- default');
	RAISE NOTICE 'Value: %', default_cnt;

	if new.is_customer = true and default_cnt = 0 THEN
  		INSERT INTO public.projects (project_name, fk_customer, planned_start_date, planned_end_date) VALUES(CONCAT(new.company_name, '- default'), new.id_company, now(), '99991231');
  	end if;
	return new;
END;
$function$
;

-- Permissions

ALTER FUNCTION public.f_create_default_project() OWNER TO hello_django;
GRANT ALL ON FUNCTION public.f_create_default_project() TO hello_django;

-- Table Triggers

create trigger default_project after
insert
    or
delete
    or
update
    on
    public.companies for each row execute function f_create_default_project();
-- Permissions

GRANT ALL ON SCHEMA public TO hello_django;
