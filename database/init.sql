--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 14.9 (Ubuntu 14.9-0ubuntu0.22.04.1)

-- Started on 2023-09-04 18:03:03 CEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 11 (class 2615 OID 16385)
-- Name: assets; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA assets;


--
-- TOC entry 5 (class 2615 OID 16386)
-- Name: employees; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA employees;


--
-- TOC entry 7 (class 2615 OID 16387)
-- Name: finances; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA finances;


--
-- TOC entry 6 (class 2615 OID 16388)
-- Name: master; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA master;


--
-- TOC entry 4 (class 2615 OID 16389)
-- Name: operations; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA operations;


--
-- TOC entry 3 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- TOC entry 3436 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- TOC entry 10 (class 2615 OID 16390)
-- Name: sys; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA sys;


--
-- TOC entry 270 (class 1255 OID 16391)
-- Name: f_create_default_project(); Type: FUNCTION; Schema: public; Owner: -
--

CREATE FUNCTION public.f_create_default_project() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
declare default_cnt integer;
begin
	SELECT count(*) INTO default_cnt FROM operations.projects WHERE project_name = CONCAT(new.company_name, '- default');
	RAISE NOTICE 'Value: %', default_cnt;

	if new.is_customer = true and default_cnt = 0 THEN
  		INSERT INTO operations.projects (project_name, fk_customer, planned_start_date, planned_end_date) VALUES(CONCAT(new.company_name, '- default'), new.id_company, now(), '99991231');
  	end if;
	return new;
END; 
$$;


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 206 (class 1259 OID 16392)
-- Name: employee_absence_codes; Type: TABLE; Schema: employees; Owner: -
--

CREATE TABLE employees.employee_absence_codes (
    id_employee_absence_code integer NOT NULL,
    employee_absence_code character varying NOT NULL,
    employee_absence_code_abbreviation character varying NOT NULL
);


--
-- TOC entry 207 (class 1259 OID 16398)
-- Name: employee_absence_code_id_employee_absence_code_seq; Type: SEQUENCE; Schema: employees; Owner: -
--

CREATE SEQUENCE employees.employee_absence_code_id_employee_absence_code_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3437 (class 0 OID 0)
-- Dependencies: 207
-- Name: employee_absence_code_id_employee_absence_code_seq; Type: SEQUENCE OWNED BY; Schema: employees; Owner: -
--

ALTER SEQUENCE employees.employee_absence_code_id_employee_absence_code_seq OWNED BY employees.employee_absence_codes.id_employee_absence_code;


--
-- TOC entry 208 (class 1259 OID 16400)
-- Name: asset_absence_codes; Type: TABLE; Schema: assets; Owner: -
--

CREATE TABLE assets.asset_absence_codes (
    id_asset_absence_code integer DEFAULT nextval('employees.employee_absence_code_id_employee_absence_code_seq'::regclass) NOT NULL,
    asset_absence_code character varying NOT NULL,
    asset_absence_code_abbreviation character varying NOT NULL
);


--
-- TOC entry 209 (class 1259 OID 16407)
-- Name: employee_absences; Type: TABLE; Schema: employees; Owner: -
--

CREATE TABLE employees.employee_absences (
    id_employee_absence integer NOT NULL,
    "from" timestamp without time zone NOT NULL,
    "to" timestamp without time zone NOT NULL,
    fk_employee integer NOT NULL,
    fk_employee_absence_code integer NOT NULL
);


--
-- TOC entry 210 (class 1259 OID 16410)
-- Name: employee_absence_id_employee_absence_seq; Type: SEQUENCE; Schema: employees; Owner: -
--

CREATE SEQUENCE employees.employee_absence_id_employee_absence_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3438 (class 0 OID 0)
-- Dependencies: 210
-- Name: employee_absence_id_employee_absence_seq; Type: SEQUENCE OWNED BY; Schema: employees; Owner: -
--

ALTER SEQUENCE employees.employee_absence_id_employee_absence_seq OWNED BY employees.employee_absences.id_employee_absence;


--
-- TOC entry 211 (class 1259 OID 16412)
-- Name: asset_absences; Type: TABLE; Schema: assets; Owner: -
--

CREATE TABLE assets.asset_absences (
    id_asset_absence integer DEFAULT nextval('employees.employee_absence_id_employee_absence_seq'::regclass) NOT NULL,
    "from" timestamp without time zone NOT NULL,
    "to" timestamp without time zone NOT NULL,
    fk_asset integer NOT NULL,
    fk_asset_absence_code integer NOT NULL
);


--
-- TOC entry 212 (class 1259 OID 16416)
-- Name: asset_types; Type: TABLE; Schema: assets; Owner: -
--

CREATE TABLE assets.asset_types (
    id_asset_type integer NOT NULL,
    asset_type character varying NOT NULL,
    max_capacity numeric
);


--
-- TOC entry 213 (class 1259 OID 16422)
-- Name: asset_types_id_asset_type_seq; Type: SEQUENCE; Schema: assets; Owner: -
--

CREATE SEQUENCE assets.asset_types_id_asset_type_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3439 (class 0 OID 0)
-- Dependencies: 213
-- Name: asset_types_id_asset_type_seq; Type: SEQUENCE OWNED BY; Schema: assets; Owner: -
--

ALTER SEQUENCE assets.asset_types_id_asset_type_seq OWNED BY assets.asset_types.id_asset_type;


--
-- TOC entry 214 (class 1259 OID 16424)
-- Name: assets; Type: TABLE; Schema: assets; Owner: -
--

CREATE TABLE assets.assets (
    id_asset integer NOT NULL,
    fk_asset_type integer NOT NULL,
    asset_description character varying NOT NULL,
    fk_employee integer,
    asset_internal_alias character varying NOT NULL,
    year_of_production integer,
    asset_km_counter character varying,
    fk_sys_rec_state integer NOT NULL
);


--
-- TOC entry 215 (class 1259 OID 16430)
-- Name: assets_id_asset_seq; Type: SEQUENCE; Schema: assets; Owner: -
--

CREATE SEQUENCE assets.assets_id_asset_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3440 (class 0 OID 0)
-- Dependencies: 215
-- Name: assets_id_asset_seq; Type: SEQUENCE OWNED BY; Schema: assets; Owner: -
--

ALTER SEQUENCE assets.assets_id_asset_seq OWNED BY assets.assets.id_asset;


--
-- TOC entry 216 (class 1259 OID 16432)
-- Name: authtoken_token; Type: TABLE; Schema: assets; Owner: -
--

CREATE TABLE assets.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


--
-- TOC entry 217 (class 1259 OID 16435)
-- Name: employees; Type: TABLE; Schema: employees; Owner: -
--

CREATE TABLE employees.employees (
    id_employee integer NOT NULL,
    employee_first_name character varying NOT NULL,
    employee_last_name character varying NOT NULL,
    employee_street character varying NOT NULL,
    employee_zipcode character varying NOT NULL,
    employee_city character varying NOT NULL,
    emplyee_email character varying NOT NULL,
    employee_cell_phone character varying NOT NULL,
    emplyee_birthday date NOT NULL,
    emplyee_salary numeric,
    fk_employee_type integer NOT NULL,
    employee_fte numeric DEFAULT 1 NOT NULL,
    employee_internal_alias character varying NOT NULL,
    fk_sys_rec_status integer NOT NULL,
    employee_house_nr character varying NOT NULL
);


--
-- TOC entry 218 (class 1259 OID 16442)
-- Name: employee_id_employee_seq; Type: SEQUENCE; Schema: employees; Owner: -
--

CREATE SEQUENCE employees.employee_id_employee_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3441 (class 0 OID 0)
-- Dependencies: 218
-- Name: employee_id_employee_seq; Type: SEQUENCE OWNED BY; Schema: employees; Owner: -
--

ALTER SEQUENCE employees.employee_id_employee_seq OWNED BY employees.employees.id_employee;


--
-- TOC entry 219 (class 1259 OID 16444)
-- Name: employee_types; Type: TABLE; Schema: employees; Owner: -
--

CREATE TABLE employees.employee_types (
    id_employee_type integer NOT NULL,
    employee_type_description character varying NOT NULL
);


--
-- TOC entry 220 (class 1259 OID 16450)
-- Name: employee_type_employee_type_seq; Type: SEQUENCE; Schema: employees; Owner: -
--

CREATE SEQUENCE employees.employee_type_employee_type_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3442 (class 0 OID 0)
-- Dependencies: 220
-- Name: employee_type_employee_type_seq; Type: SEQUENCE OWNED BY; Schema: employees; Owner: -
--

ALTER SEQUENCE employees.employee_type_employee_type_seq OWNED BY employees.employee_types.id_employee_type;


--
-- TOC entry 221 (class 1259 OID 16452)
-- Name: currencies; Type: TABLE; Schema: finances; Owner: -
--

CREATE TABLE finances.currencies (
    id_currency integer NOT NULL,
    currency character varying NOT NULL,
    currency_abbreviation character varying NOT NULL,
    currency_account_nr character varying NOT NULL
);


--
-- TOC entry 222 (class 1259 OID 16458)
-- Name: curency_id_currency_seq; Type: SEQUENCE; Schema: finances; Owner: -
--

CREATE SEQUENCE finances.curency_id_currency_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3443 (class 0 OID 0)
-- Dependencies: 222
-- Name: curency_id_currency_seq; Type: SEQUENCE OWNED BY; Schema: finances; Owner: -
--

ALTER SEQUENCE finances.curency_id_currency_seq OWNED BY finances.currencies.id_currency;


--
-- TOC entry 223 (class 1259 OID 16460)
-- Name: invoice_texts; Type: TABLE; Schema: finances; Owner: -
--

CREATE TABLE finances.invoice_texts (
    id_invoice_text integer NOT NULL,
    invoice_text character varying NOT NULL,
    fk_customer integer NOT NULL
);


--
-- TOC entry 224 (class 1259 OID 16466)
-- Name: customer_invoice_text_id_customer_invoice_text_seq; Type: SEQUENCE; Schema: finances; Owner: -
--

CREATE SEQUENCE finances.customer_invoice_text_id_customer_invoice_text_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3444 (class 0 OID 0)
-- Dependencies: 224
-- Name: customer_invoice_text_id_customer_invoice_text_seq; Type: SEQUENCE OWNED BY; Schema: finances; Owner: -
--

ALTER SEQUENCE finances.customer_invoice_text_id_customer_invoice_text_seq OWNED BY finances.invoice_texts.id_invoice_text;


--
-- TOC entry 225 (class 1259 OID 16468)
-- Name: invoices; Type: TABLE; Schema: finances; Owner: -
--

CREATE TABLE finances.invoices (
    id_invoice integer NOT NULL,
    invoice_date date,
    fk_invoice_text integer,
    fk_invoice_state integer NOT NULL,
    fk_payment_conditions integer NOT NULL
);


--
-- TOC entry 226 (class 1259 OID 16471)
-- Name: invoice_id_invoice_seq; Type: SEQUENCE; Schema: finances; Owner: -
--

CREATE SEQUENCE finances.invoice_id_invoice_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3445 (class 0 OID 0)
-- Dependencies: 226
-- Name: invoice_id_invoice_seq; Type: SEQUENCE OWNED BY; Schema: finances; Owner: -
--

ALTER SEQUENCE finances.invoice_id_invoice_seq OWNED BY finances.invoices.id_invoice;


--
-- TOC entry 227 (class 1259 OID 16473)
-- Name: invoice_states; Type: TABLE; Schema: finances; Owner: -
--

CREATE TABLE finances.invoice_states (
    id_invoice_state integer NOT NULL,
    invoice_state character varying NOT NULL,
    invoice_state_abbreviation integer NOT NULL
);


--
-- TOC entry 228 (class 1259 OID 16479)
-- Name: invoice_status_id_invoice_status_seq; Type: SEQUENCE; Schema: finances; Owner: -
--

CREATE SEQUENCE finances.invoice_status_id_invoice_status_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3446 (class 0 OID 0)
-- Dependencies: 228
-- Name: invoice_status_id_invoice_status_seq; Type: SEQUENCE OWNED BY; Schema: finances; Owner: -
--

ALTER SEQUENCE finances.invoice_status_id_invoice_status_seq OWNED BY finances.invoice_states.id_invoice_state;


--
-- TOC entry 229 (class 1259 OID 16481)
-- Name: payment_conditions; Type: TABLE; Schema: finances; Owner: -
--

CREATE TABLE finances.payment_conditions (
    id_payment_condition integer NOT NULL,
    vat numeric NOT NULL,
    fk_currency integer NOT NULL,
    due_days integer NOT NULL
);


--
-- TOC entry 230 (class 1259 OID 16487)
-- Name: payment_conditions_id_payment_condition_seq; Type: SEQUENCE; Schema: finances; Owner: -
--

CREATE SEQUENCE finances.payment_conditions_id_payment_condition_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3447 (class 0 OID 0)
-- Dependencies: 230
-- Name: payment_conditions_id_payment_condition_seq; Type: SEQUENCE OWNED BY; Schema: finances; Owner: -
--

ALTER SEQUENCE finances.payment_conditions_id_payment_condition_seq OWNED BY finances.payment_conditions.id_payment_condition;


--
-- TOC entry 231 (class 1259 OID 16489)
-- Name: companies; Type: TABLE; Schema: master; Owner: -
--

CREATE TABLE master.companies (
    id_company integer NOT NULL,
    company_name character varying NOT NULL,
    company_street character varying NOT NULL,
    company_zipcode character varying NOT NULL,
    company_country character varying NOT NULL,
    company_city character varying NOT NULL,
    company_internal_alias character varying NOT NULL,
    fk_sys_rec_status integer NOT NULL,
    company_email character varying,
    is_customer boolean,
    is_supplier boolean,
    is_subcontractor boolean
);


--
-- TOC entry 232 (class 1259 OID 16495)
-- Name: newtable_id_customer_seq; Type: SEQUENCE; Schema: master; Owner: -
--

CREATE SEQUENCE master.newtable_id_customer_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3448 (class 0 OID 0)
-- Dependencies: 232
-- Name: newtable_id_customer_seq; Type: SEQUENCE OWNED BY; Schema: master; Owner: -
--

ALTER SEQUENCE master.newtable_id_customer_seq OWNED BY master.companies.id_company;


--
-- TOC entry 267 (class 1259 OID 16910)
-- Name: asset_allocation; Type: TABLE; Schema: operations; Owner: -
--

CREATE TABLE operations.asset_allocation (
    id_asset_allocation integer NOT NULL,
    fk_asset integer NOT NULL,
    fk_task integer NOT NULL
);


--
-- TOC entry 266 (class 1259 OID 16908)
-- Name: asset_allocation_id_asset_allocation_seq; Type: SEQUENCE; Schema: operations; Owner: -
--

CREATE SEQUENCE operations.asset_allocation_id_asset_allocation_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3449 (class 0 OID 0)
-- Dependencies: 266
-- Name: asset_allocation_id_asset_allocation_seq; Type: SEQUENCE OWNED BY; Schema: operations; Owner: -
--

ALTER SEQUENCE operations.asset_allocation_id_asset_allocation_seq OWNED BY operations.asset_allocation.id_asset_allocation;


--
-- TOC entry 269 (class 1259 OID 16930)
-- Name: employee_allocation; Type: TABLE; Schema: operations; Owner: -
--

CREATE TABLE operations.employee_allocation (
    id_employee_allocation integer NOT NULL,
    fk_task integer NOT NULL,
    fk_employee integer NOT NULL
);


--
-- TOC entry 268 (class 1259 OID 16928)
-- Name: employee_allocation_id_employee_allocation_seq; Type: SEQUENCE; Schema: operations; Owner: -
--

CREATE SEQUENCE operations.employee_allocation_id_employee_allocation_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3450 (class 0 OID 0)
-- Dependencies: 268
-- Name: employee_allocation_id_employee_allocation_seq; Type: SEQUENCE OWNED BY; Schema: operations; Owner: -
--

ALTER SEQUENCE operations.employee_allocation_id_employee_allocation_seq OWNED BY operations.employee_allocation.id_employee_allocation;


--
-- TOC entry 233 (class 1259 OID 16497)
-- Name: projects; Type: TABLE; Schema: operations; Owner: -
--

CREATE TABLE operations.projects (
    id_project integer NOT NULL,
    project_name character varying NOT NULL,
    fk_customer integer NOT NULL,
    planned_start_date date NOT NULL,
    planned_end_date date NOT NULL,
    effective_start_date date,
    effective_end_date date
);


--
-- TOC entry 234 (class 1259 OID 16503)
-- Name: projects_id_project_seq; Type: SEQUENCE; Schema: operations; Owner: -
--

CREATE SEQUENCE operations.projects_id_project_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3451 (class 0 OID 0)
-- Dependencies: 234
-- Name: projects_id_project_seq; Type: SEQUENCE OWNED BY; Schema: operations; Owner: -
--

ALTER SEQUENCE operations.projects_id_project_seq OWNED BY operations.projects.id_project;


--
-- TOC entry 235 (class 1259 OID 16505)
-- Name: sales; Type: TABLE; Schema: operations; Owner: -
--

CREATE TABLE operations.sales (
    id_sale integer NOT NULL,
    sale_timestamp timestamp without time zone NOT NULL,
    fk_project integer NOT NULL,
    sale_amount numeric NOT NULL,
    sale_unit_price numeric NOT NULL,
    sales_reference character varying NOT NULL,
    fk_unit integer NOT NULL,
    fk_product integer NOT NULL,
    fk_invoice integer NOT NULL
);


--
-- TOC entry 236 (class 1259 OID 16511)
-- Name: sales_id_sale_seq; Type: SEQUENCE; Schema: operations; Owner: -
--

CREATE SEQUENCE operations.sales_id_sale_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3452 (class 0 OID 0)
-- Dependencies: 236
-- Name: sales_id_sale_seq; Type: SEQUENCE OWNED BY; Schema: operations; Owner: -
--

ALTER SEQUENCE operations.sales_id_sale_seq OWNED BY operations.sales.id_sale;


--
-- TOC entry 237 (class 1259 OID 16513)
-- Name: task_states; Type: TABLE; Schema: operations; Owner: -
--

CREATE TABLE operations.task_states (
    id_task_state integer NOT NULL,
    task_state character varying NOT NULL
);


--
-- TOC entry 238 (class 1259 OID 16519)
-- Name: service_states_id_service_state_seq; Type: SEQUENCE; Schema: operations; Owner: -
--

CREATE SEQUENCE operations.service_states_id_service_state_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3453 (class 0 OID 0)
-- Dependencies: 238
-- Name: service_states_id_service_state_seq; Type: SEQUENCE OWNED BY; Schema: operations; Owner: -
--

ALTER SEQUENCE operations.service_states_id_service_state_seq OWNED BY operations.task_states.id_task_state;


--
-- TOC entry 239 (class 1259 OID 16521)
-- Name: task_templates; Type: TABLE; Schema: operations; Owner: -
--

CREATE TABLE operations.task_templates (
    id_task_template integer NOT NULL,
    fk_customer integer NOT NULL,
    fk_unit integer NOT NULL,
    amount numeric NOT NULL,
    unit_price numeric NOT NULL,
    task_description character varying NOT NULL
);


--
-- TOC entry 240 (class 1259 OID 16527)
-- Name: service_templates_id_service_template_seq; Type: SEQUENCE; Schema: operations; Owner: -
--

CREATE SEQUENCE operations.service_templates_id_service_template_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3454 (class 0 OID 0)
-- Dependencies: 240
-- Name: service_templates_id_service_template_seq; Type: SEQUENCE OWNED BY; Schema: operations; Owner: -
--

ALTER SEQUENCE operations.service_templates_id_service_template_seq OWNED BY operations.task_templates.id_task_template;


--
-- TOC entry 241 (class 1259 OID 16529)
-- Name: tasks; Type: TABLE; Schema: operations; Owner: -
--

CREATE TABLE operations.tasks (
    id_task integer NOT NULL,
    fk_project integer NOT NULL,
    fk_task_state integer NOT NULL,
    timestamp_from timestamp without time zone,
    timestamp_to timestamp without time zone,
    amount numeric,
    unit_price numeric,
    task_description character varying NOT NULL,
    fk_invoice integer,
    fk_unit integer,
    fk_asset_allocation integer,
    internal_info character varying,
    customer_reference character varying,
    fk_subcontractor integer,
    brokerage_fee numeric,
    fk_service_type integer NOT NULL
);


--
-- TOC entry 242 (class 1259 OID 16535)
-- Name: services_id_service_seq; Type: SEQUENCE; Schema: operations; Owner: -
--

CREATE SEQUENCE operations.services_id_service_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3455 (class 0 OID 0)
-- Dependencies: 242
-- Name: services_id_service_seq; Type: SEQUENCE OWNED BY; Schema: operations; Owner: -
--

ALTER SEQUENCE operations.services_id_service_seq OWNED BY operations.tasks.id_task;


--
-- TOC entry 243 (class 1259 OID 16537)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


--
-- TOC entry 244 (class 1259 OID 16540)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 245 (class 1259 OID 16542)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- TOC entry 246 (class 1259 OID 16545)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 247 (class 1259 OID 16547)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- TOC entry 248 (class 1259 OID 16550)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 249 (class 1259 OID 16552)
-- Name: auth_user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


--
-- TOC entry 250 (class 1259 OID 16558)
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- TOC entry 251 (class 1259 OID 16561)
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_user_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 252 (class 1259 OID 16563)
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 253 (class 1259 OID 16565)
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- TOC entry 254 (class 1259 OID 16568)
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 255 (class 1259 OID 16570)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


--
-- TOC entry 256 (class 1259 OID 16577)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 257 (class 1259 OID 16579)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- TOC entry 258 (class 1259 OID 16582)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 259 (class 1259 OID 16584)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- TOC entry 260 (class 1259 OID 16590)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 261 (class 1259 OID 16592)
-- Name: django_session; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- TOC entry 262 (class 1259 OID 16598)
-- Name: sys_rec_states; Type: TABLE; Schema: sys; Owner: -
--

CREATE TABLE sys.sys_rec_states (
    id_sys_rec_status integer NOT NULL,
    sys_rec_status character varying NOT NULL
);


--
-- TOC entry 263 (class 1259 OID 16604)
-- Name: sys_rec_states_id_sys_rec_status_seq; Type: SEQUENCE; Schema: sys; Owner: -
--

CREATE SEQUENCE sys.sys_rec_states_id_sys_rec_status_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3456 (class 0 OID 0)
-- Dependencies: 263
-- Name: sys_rec_states_id_sys_rec_status_seq; Type: SEQUENCE OWNED BY; Schema: sys; Owner: -
--

ALTER SEQUENCE sys.sys_rec_states_id_sys_rec_status_seq OWNED BY sys.sys_rec_states.id_sys_rec_status;


--
-- TOC entry 264 (class 1259 OID 16606)
-- Name: units; Type: TABLE; Schema: sys; Owner: -
--

CREATE TABLE sys.units (
    id_unit integer NOT NULL,
    unit character varying NOT NULL,
    unit_abbreviation character varying NOT NULL
);


--
-- TOC entry 265 (class 1259 OID 16612)
-- Name: units_id_unit_seq; Type: SEQUENCE; Schema: sys; Owner: -
--

CREATE SEQUENCE sys.units_id_unit_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3457 (class 0 OID 0)
-- Dependencies: 265
-- Name: units_id_unit_seq; Type: SEQUENCE OWNED BY; Schema: sys; Owner: -
--

ALTER SEQUENCE sys.units_id_unit_seq OWNED BY sys.units.id_unit;


--
-- TOC entry 3073 (class 2604 OID 16614)
-- Name: asset_types id_asset_type; Type: DEFAULT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_types ALTER COLUMN id_asset_type SET DEFAULT nextval('assets.asset_types_id_asset_type_seq'::regclass);


--
-- TOC entry 3074 (class 2604 OID 16615)
-- Name: assets id_asset; Type: DEFAULT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.assets ALTER COLUMN id_asset SET DEFAULT nextval('assets.assets_id_asset_seq'::regclass);


--
-- TOC entry 3069 (class 2604 OID 16616)
-- Name: employee_absence_codes id_employee_absence_code; Type: DEFAULT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_absence_codes ALTER COLUMN id_employee_absence_code SET DEFAULT nextval('employees.employee_absence_code_id_employee_absence_code_seq'::regclass);


--
-- TOC entry 3071 (class 2604 OID 16617)
-- Name: employee_absences id_employee_absence; Type: DEFAULT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_absences ALTER COLUMN id_employee_absence SET DEFAULT nextval('employees.employee_absence_id_employee_absence_seq'::regclass);


--
-- TOC entry 3077 (class 2604 OID 16618)
-- Name: employee_types id_employee_type; Type: DEFAULT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_types ALTER COLUMN id_employee_type SET DEFAULT nextval('employees.employee_type_employee_type_seq'::regclass);


--
-- TOC entry 3076 (class 2604 OID 16619)
-- Name: employees id_employee; Type: DEFAULT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employees ALTER COLUMN id_employee SET DEFAULT nextval('employees.employee_id_employee_seq'::regclass);


--
-- TOC entry 3078 (class 2604 OID 16620)
-- Name: currencies id_currency; Type: DEFAULT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.currencies ALTER COLUMN id_currency SET DEFAULT nextval('finances.curency_id_currency_seq'::regclass);


--
-- TOC entry 3081 (class 2604 OID 16621)
-- Name: invoice_states id_invoice_state; Type: DEFAULT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.invoice_states ALTER COLUMN id_invoice_state SET DEFAULT nextval('finances.invoice_status_id_invoice_status_seq'::regclass);


--
-- TOC entry 3079 (class 2604 OID 16622)
-- Name: invoice_texts id_invoice_text; Type: DEFAULT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.invoice_texts ALTER COLUMN id_invoice_text SET DEFAULT nextval('finances.customer_invoice_text_id_customer_invoice_text_seq'::regclass);


--
-- TOC entry 3080 (class 2604 OID 16623)
-- Name: invoices id_invoice; Type: DEFAULT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.invoices ALTER COLUMN id_invoice SET DEFAULT nextval('finances.invoice_id_invoice_seq'::regclass);


--
-- TOC entry 3082 (class 2604 OID 16624)
-- Name: payment_conditions id_payment_condition; Type: DEFAULT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.payment_conditions ALTER COLUMN id_payment_condition SET DEFAULT nextval('finances.payment_conditions_id_payment_condition_seq'::regclass);


--
-- TOC entry 3083 (class 2604 OID 16625)
-- Name: companies id_company; Type: DEFAULT; Schema: master; Owner: -
--

ALTER TABLE ONLY master.companies ALTER COLUMN id_company SET DEFAULT nextval('master.newtable_id_customer_seq'::regclass);


--
-- TOC entry 3092 (class 2604 OID 16913)
-- Name: asset_allocation id_asset_allocation; Type: DEFAULT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.asset_allocation ALTER COLUMN id_asset_allocation SET DEFAULT nextval('operations.asset_allocation_id_asset_allocation_seq'::regclass);


--
-- TOC entry 3093 (class 2604 OID 16933)
-- Name: employee_allocation id_employee_allocation; Type: DEFAULT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.employee_allocation ALTER COLUMN id_employee_allocation SET DEFAULT nextval('operations.employee_allocation_id_employee_allocation_seq'::regclass);


--
-- TOC entry 3084 (class 2604 OID 16626)
-- Name: projects id_project; Type: DEFAULT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.projects ALTER COLUMN id_project SET DEFAULT nextval('operations.projects_id_project_seq'::regclass);


--
-- TOC entry 3085 (class 2604 OID 16627)
-- Name: sales id_sale; Type: DEFAULT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.sales ALTER COLUMN id_sale SET DEFAULT nextval('operations.sales_id_sale_seq'::regclass);


--
-- TOC entry 3086 (class 2604 OID 16628)
-- Name: task_states id_task_state; Type: DEFAULT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.task_states ALTER COLUMN id_task_state SET DEFAULT nextval('operations.service_states_id_service_state_seq'::regclass);


--
-- TOC entry 3087 (class 2604 OID 16629)
-- Name: task_templates id_task_template; Type: DEFAULT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.task_templates ALTER COLUMN id_task_template SET DEFAULT nextval('operations.service_templates_id_service_template_seq'::regclass);


--
-- TOC entry 3088 (class 2604 OID 16630)
-- Name: tasks id_task; Type: DEFAULT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.tasks ALTER COLUMN id_task SET DEFAULT nextval('operations.services_id_service_seq'::regclass);


--
-- TOC entry 3090 (class 2604 OID 16631)
-- Name: sys_rec_states id_sys_rec_status; Type: DEFAULT; Schema: sys; Owner: -
--

ALTER TABLE ONLY sys.sys_rec_states ALTER COLUMN id_sys_rec_status SET DEFAULT nextval('sys.sys_rec_states_id_sys_rec_status_seq'::regclass);


--
-- TOC entry 3091 (class 2604 OID 16632)
-- Name: units id_unit; Type: DEFAULT; Schema: sys; Owner: -
--

ALTER TABLE ONLY sys.units ALTER COLUMN id_unit SET DEFAULT nextval('sys.units_id_unit_seq'::regclass);


--
-- TOC entry 3369 (class 0 OID 16400)
-- Dependencies: 208
-- Data for Name: asset_absence_codes; Type: TABLE DATA; Schema: assets; Owner: -
--

COPY assets.asset_absence_codes (id_asset_absence_code, asset_absence_code, asset_absence_code_abbreviation) FROM stdin;
1	Maintanance	Mt
2	Rented	Rt
3	Defect	Dt
4	Inspection	In
5	Repair	R
\.


--
-- TOC entry 3372 (class 0 OID 16412)
-- Dependencies: 211
-- Data for Name: asset_absences; Type: TABLE DATA; Schema: assets; Owner: -
--

COPY assets.asset_absences (id_asset_absence, "from", "to", fk_asset, fk_asset_absence_code) FROM stdin;
\.


--
-- TOC entry 3373 (class 0 OID 16416)
-- Dependencies: 212
-- Data for Name: asset_types; Type: TABLE DATA; Schema: assets; Owner: -
--

COPY assets.asset_types (id_asset_type, asset_type, max_capacity) FROM stdin;
1	Car	\N
2	Truck	\N
3	Trailers	\N
\.


--
-- TOC entry 3375 (class 0 OID 16424)
-- Dependencies: 214
-- Data for Name: assets; Type: TABLE DATA; Schema: assets; Owner: -
--

COPY assets.assets (id_asset, fk_asset_type, asset_description, fk_employee, asset_internal_alias, year_of_production, asset_km_counter, fk_sys_rec_state) FROM stdin;
\.


--
-- TOC entry 3377 (class 0 OID 16432)
-- Dependencies: 216
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: assets; Owner: -
--

COPY assets.authtoken_token (key, created, user_id) FROM stdin;
9455c458297b4c109d2e5c65b67ce303c13b52ac	2023-08-06 15:54:03.750143+00	1
\.


--
-- TOC entry 3367 (class 0 OID 16392)
-- Dependencies: 206
-- Data for Name: employee_absence_codes; Type: TABLE DATA; Schema: employees; Owner: -
--

COPY employees.employee_absence_codes (id_employee_absence_code, employee_absence_code, employee_absence_code_abbreviation) FROM stdin;
\.


--
-- TOC entry 3370 (class 0 OID 16407)
-- Dependencies: 209
-- Data for Name: employee_absences; Type: TABLE DATA; Schema: employees; Owner: -
--

COPY employees.employee_absences (id_employee_absence, "from", "to", fk_employee, fk_employee_absence_code) FROM stdin;
\.


--
-- TOC entry 3380 (class 0 OID 16444)
-- Dependencies: 219
-- Data for Name: employee_types; Type: TABLE DATA; Schema: employees; Owner: -
--

COPY employees.employee_types (id_employee_type, employee_type_description) FROM stdin;
\.


--
-- TOC entry 3378 (class 0 OID 16435)
-- Dependencies: 217
-- Data for Name: employees; Type: TABLE DATA; Schema: employees; Owner: -
--

COPY employees.employees (id_employee, employee_first_name, employee_last_name, employee_street, employee_zipcode, employee_city, emplyee_email, employee_cell_phone, emplyee_birthday, emplyee_salary, fk_employee_type, employee_fte, employee_internal_alias, fk_sys_rec_status, employee_house_nr) FROM stdin;
\.


--
-- TOC entry 3382 (class 0 OID 16452)
-- Dependencies: 221
-- Data for Name: currencies; Type: TABLE DATA; Schema: finances; Owner: -
--

COPY finances.currencies (id_currency, currency, currency_abbreviation, currency_account_nr) FROM stdin;
1	Schweizer Franken	CHF	1
\.


--
-- TOC entry 3388 (class 0 OID 16473)
-- Dependencies: 227
-- Data for Name: invoice_states; Type: TABLE DATA; Schema: finances; Owner: -
--

COPY finances.invoice_states (id_invoice_state, invoice_state, invoice_state_abbreviation) FROM stdin;
\.


--
-- TOC entry 3384 (class 0 OID 16460)
-- Dependencies: 223
-- Data for Name: invoice_texts; Type: TABLE DATA; Schema: finances; Owner: -
--

COPY finances.invoice_texts (id_invoice_text, invoice_text, fk_customer) FROM stdin;
\.


--
-- TOC entry 3386 (class 0 OID 16468)
-- Dependencies: 225
-- Data for Name: invoices; Type: TABLE DATA; Schema: finances; Owner: -
--

COPY finances.invoices (id_invoice, invoice_date, fk_invoice_text, fk_invoice_state, fk_payment_conditions) FROM stdin;
\.


--
-- TOC entry 3390 (class 0 OID 16481)
-- Dependencies: 229
-- Data for Name: payment_conditions; Type: TABLE DATA; Schema: finances; Owner: -
--

COPY finances.payment_conditions (id_payment_condition, vat, fk_currency, due_days) FROM stdin;
\.


--
-- TOC entry 3392 (class 0 OID 16489)
-- Dependencies: 231
-- Data for Name: companies; Type: TABLE DATA; Schema: master; Owner: -
--

COPY master.companies (id_company, company_name, company_street, company_zipcode, company_country, company_city, company_internal_alias, fk_sys_rec_status, company_email, is_customer, is_supplier, is_subcontractor) FROM stdin;
32	test1	test1	teset	test	test	stest1	1	asdfadfasdfasdfafd	t	f	f
33	asdfasdf	asdfasdf	asdfasf	asdfasdf	zzzzzzz	asdfasdf	1	asdfasfd	t	t	t
31	Pfister Transporte AG	Buchsistrasse 10	3380	Schweiz	Wangen an der Aare	Zwangslager	1	info@pfister-transporte.ch	t	f	f
34	Data Dudes	Zürichstrasse 9	6004	Schweiz	Luzern	DD	1	info@data-dudes.ch	t	f	f
\.


--
-- TOC entry 3428 (class 0 OID 16910)
-- Dependencies: 267
-- Data for Name: asset_allocation; Type: TABLE DATA; Schema: operations; Owner: -
--

COPY operations.asset_allocation (id_asset_allocation, fk_asset, fk_task) FROM stdin;
\.


--
-- TOC entry 3430 (class 0 OID 16930)
-- Dependencies: 269
-- Data for Name: employee_allocation; Type: TABLE DATA; Schema: operations; Owner: -
--

COPY operations.employee_allocation (id_employee_allocation, fk_task, fk_employee) FROM stdin;
\.


--
-- TOC entry 3394 (class 0 OID 16497)
-- Dependencies: 233
-- Data for Name: projects; Type: TABLE DATA; Schema: operations; Owner: -
--

COPY operations.projects (id_project, project_name, fk_customer, planned_start_date, planned_end_date, effective_start_date, effective_end_date) FROM stdin;
2	test1- default	32	2023-08-18	9999-12-31	\N	\N
3	test- default	31	2023-08-18	9999-12-31	\N	\N
4	asdfasdf- default	33	2023-09-04	9999-12-31	\N	\N
5	Pfister Transporte AG- default	31	2023-09-04	9999-12-31	\N	\N
6	Data Dudes- default	34	2023-09-04	9999-12-31	\N	\N
\.


--
-- TOC entry 3396 (class 0 OID 16505)
-- Dependencies: 235
-- Data for Name: sales; Type: TABLE DATA; Schema: operations; Owner: -
--

COPY operations.sales (id_sale, sale_timestamp, fk_project, sale_amount, sale_unit_price, sales_reference, fk_unit, fk_product, fk_invoice) FROM stdin;
\.


--
-- TOC entry 3398 (class 0 OID 16513)
-- Dependencies: 237
-- Data for Name: task_states; Type: TABLE DATA; Schema: operations; Owner: -
--

COPY operations.task_states (id_task_state, task_state) FROM stdin;
\.


--
-- TOC entry 3400 (class 0 OID 16521)
-- Dependencies: 239
-- Data for Name: task_templates; Type: TABLE DATA; Schema: operations; Owner: -
--

COPY operations.task_templates (id_task_template, fk_customer, fk_unit, amount, unit_price, task_description) FROM stdin;
\.


--
-- TOC entry 3402 (class 0 OID 16529)
-- Dependencies: 241
-- Data for Name: tasks; Type: TABLE DATA; Schema: operations; Owner: -
--

COPY operations.tasks (id_task, fk_project, fk_task_state, timestamp_from, timestamp_to, amount, unit_price, task_description, fk_invoice, fk_unit, fk_asset_allocation, internal_info, customer_reference, fk_subcontractor, brokerage_fee, fk_service_type) FROM stdin;
\.


--
-- TOC entry 3404 (class 0 OID 16537)
-- Dependencies: 243
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- TOC entry 3406 (class 0 OID 16542)
-- Dependencies: 245
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- TOC entry 3408 (class 0 OID 16547)
-- Dependencies: 247
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add Token	7	add_token
26	Can change Token	7	change_token
27	Can delete Token	7	delete_token
28	Can view Token	7	view_token
29	Can add token	8	add_tokenproxy
30	Can change token	8	change_tokenproxy
31	Can delete token	8	delete_tokenproxy
32	Can view token	8	view_tokenproxy
\.


--
-- TOC entry 3410 (class 0 OID 16552)
-- Dependencies: 249
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$600000$e6A3MsMUk67nlNbTMNUc5d$wzTHfCyQ4F679y2eSRH1NGx6HjsJQL9wj7MsOxq7xo8=	2023-08-06 15:50:51.000064+00	t	sisyphus				t	t	2023-08-06 15:50:29.624249+00
2	pbkdf2_sha256$600000$lzh13IjLcYIsS2hiYbLRqC$uDF/7C/NYE8jlwRA9tLX42wiFLZhgkibIld/Ze1gkuE=	2023-08-18 16:09:36.160586+00	t	fabian				t	t	2023-08-18 16:09:19.460986+00
\.


--
-- TOC entry 3411 (class 0 OID 16558)
-- Dependencies: 250
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- TOC entry 3414 (class 0 OID 16565)
-- Dependencies: 253
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- TOC entry 3416 (class 0 OID 16570)
-- Dependencies: 255
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2023-08-06 15:54:03.750614+00	1	9455c458297b4c109d2e5c65b67ce303c13b52ac	1	[{"added": {}}]	8	1
\.


--
-- TOC entry 3418 (class 0 OID 16579)
-- Dependencies: 257
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	authtoken	token
8	authtoken	tokenproxy
\.


--
-- TOC entry 3420 (class 0 OID 16584)
-- Dependencies: 259
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2023-08-03 18:05:02.09822+00
2	auth	0001_initial	2023-08-03 18:05:02.174262+00
3	admin	0001_initial	2023-08-03 18:05:02.190149+00
4	admin	0002_logentry_remove_auto_add	2023-08-03 18:05:02.194585+00
5	admin	0003_logentry_add_action_flag_choices	2023-08-03 18:05:02.198644+00
6	contenttypes	0002_remove_content_type_name	2023-08-03 18:05:02.205581+00
7	auth	0002_alter_permission_name_max_length	2023-08-03 18:05:02.209523+00
8	auth	0003_alter_user_email_max_length	2023-08-03 18:05:02.21353+00
9	auth	0004_alter_user_username_opts	2023-08-03 18:05:02.217969+00
10	auth	0005_alter_user_last_login_null	2023-08-03 18:05:02.221866+00
11	auth	0006_require_contenttypes_0002	2023-08-03 18:05:02.223257+00
12	auth	0007_alter_validators_add_error_messages	2023-08-03 18:05:02.226847+00
13	auth	0008_alter_user_username_max_length	2023-08-03 18:05:02.23311+00
14	auth	0009_alter_user_last_name_max_length	2023-08-03 18:05:02.237049+00
15	auth	0010_alter_group_name_max_length	2023-08-03 18:05:02.241336+00
16	auth	0011_update_proxy_permissions	2023-08-03 18:05:02.245309+00
17	auth	0012_alter_user_first_name_max_length	2023-08-03 18:05:02.249106+00
18	sessions	0001_initial	2023-08-03 18:05:02.262112+00
19	authtoken	0001_initial	2023-08-06 15:45:56.809255+00
20	authtoken	0002_auto_20160226_1747	2023-08-06 15:45:56.821607+00
21	authtoken	0003_tokenproxy	2023-08-06 15:45:56.823976+00
\.


--
-- TOC entry 3422 (class 0 OID 16592)
-- Dependencies: 261
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
51gop5y9xk05govqecdalhlt31tih0ha	.eJxVjEEOgyAURK_SsK7mA4LWZfc9A4H_odgabASbNE3vXk3cuJvMezNf9lpyNNmnwvq0jOOZjTYXY7EM76F8WM8ECFlBV_HuxHUPl15qdmbGLiWaJfvZDLRZx85ZfPq0AXrYdJ9qnFKZB1dvSr3TXN8m8uN1dw8H0ea4rsEBKeqkJs0JW4VyjY12sgXBRQDwVglClIF8h40A7WzLXeABRatVYL8_8A1Igg:1qX22a:iWLww0E1bG5NKq5uSst8iHjdy_Oyr8f3VfQ36T_fpjU	2023-09-01 16:09:36.162747+00
\.


--
-- TOC entry 3423 (class 0 OID 16598)
-- Dependencies: 262
-- Data for Name: sys_rec_states; Type: TABLE DATA; Schema: sys; Owner: -
--

COPY sys.sys_rec_states (id_sys_rec_status, sys_rec_status) FROM stdin;
1	active
2	passive
3	left_the_company
4	sold
\.


--
-- TOC entry 3425 (class 0 OID 16606)
-- Dependencies: 264
-- Data for Name: units; Type: TABLE DATA; Schema: sys; Owner: -
--

COPY sys.units (id_unit, unit, unit_abbreviation) FROM stdin;
1	Tonne	t
2	Kilogram	kg
3	Gram	g
4	Milligram	mg
5	Meter	m
6	Millimeter	mm
7	Zentimeter	cm
8	Decimeter	dm
9	Kilometer	km
10	Squearemeter	qm
11	Liter	l
12	Milliliter	ml
13	Centiliter	cl
14	Deciliter	dl
15	Seconds	s
16	Minutes	m
17	Hours	h
18	Days	d
19	Years	y
20	Loading meter	ldm
21	Flat-rate	flat-rate
\.


--
-- TOC entry 3458 (class 0 OID 0)
-- Dependencies: 213
-- Name: asset_types_id_asset_type_seq; Type: SEQUENCE SET; Schema: assets; Owner: -
--

SELECT pg_catalog.setval('assets.asset_types_id_asset_type_seq', 3, true);


--
-- TOC entry 3459 (class 0 OID 0)
-- Dependencies: 215
-- Name: assets_id_asset_seq; Type: SEQUENCE SET; Schema: assets; Owner: -
--

SELECT pg_catalog.setval('assets.assets_id_asset_seq', 1, false);


--
-- TOC entry 3460 (class 0 OID 0)
-- Dependencies: 207
-- Name: employee_absence_code_id_employee_absence_code_seq; Type: SEQUENCE SET; Schema: employees; Owner: -
--

SELECT pg_catalog.setval('employees.employee_absence_code_id_employee_absence_code_seq', 6, true);


--
-- TOC entry 3461 (class 0 OID 0)
-- Dependencies: 210
-- Name: employee_absence_id_employee_absence_seq; Type: SEQUENCE SET; Schema: employees; Owner: -
--

SELECT pg_catalog.setval('employees.employee_absence_id_employee_absence_seq', 1, false);


--
-- TOC entry 3462 (class 0 OID 0)
-- Dependencies: 218
-- Name: employee_id_employee_seq; Type: SEQUENCE SET; Schema: employees; Owner: -
--

SELECT pg_catalog.setval('employees.employee_id_employee_seq', 1, true);


--
-- TOC entry 3463 (class 0 OID 0)
-- Dependencies: 220
-- Name: employee_type_employee_type_seq; Type: SEQUENCE SET; Schema: employees; Owner: -
--

SELECT pg_catalog.setval('employees.employee_type_employee_type_seq', 1, false);


--
-- TOC entry 3464 (class 0 OID 0)
-- Dependencies: 222
-- Name: curency_id_currency_seq; Type: SEQUENCE SET; Schema: finances; Owner: -
--

SELECT pg_catalog.setval('finances.curency_id_currency_seq', 1, true);


--
-- TOC entry 3465 (class 0 OID 0)
-- Dependencies: 224
-- Name: customer_invoice_text_id_customer_invoice_text_seq; Type: SEQUENCE SET; Schema: finances; Owner: -
--

SELECT pg_catalog.setval('finances.customer_invoice_text_id_customer_invoice_text_seq', 1, false);


--
-- TOC entry 3466 (class 0 OID 0)
-- Dependencies: 226
-- Name: invoice_id_invoice_seq; Type: SEQUENCE SET; Schema: finances; Owner: -
--

SELECT pg_catalog.setval('finances.invoice_id_invoice_seq', 1, false);


--
-- TOC entry 3467 (class 0 OID 0)
-- Dependencies: 228
-- Name: invoice_status_id_invoice_status_seq; Type: SEQUENCE SET; Schema: finances; Owner: -
--

SELECT pg_catalog.setval('finances.invoice_status_id_invoice_status_seq', 1, false);


--
-- TOC entry 3468 (class 0 OID 0)
-- Dependencies: 230
-- Name: payment_conditions_id_payment_condition_seq; Type: SEQUENCE SET; Schema: finances; Owner: -
--

SELECT pg_catalog.setval('finances.payment_conditions_id_payment_condition_seq', 1, false);


--
-- TOC entry 3469 (class 0 OID 0)
-- Dependencies: 232
-- Name: newtable_id_customer_seq; Type: SEQUENCE SET; Schema: master; Owner: -
--

SELECT pg_catalog.setval('master.newtable_id_customer_seq', 34, true);


--
-- TOC entry 3470 (class 0 OID 0)
-- Dependencies: 266
-- Name: asset_allocation_id_asset_allocation_seq; Type: SEQUENCE SET; Schema: operations; Owner: -
--

SELECT pg_catalog.setval('operations.asset_allocation_id_asset_allocation_seq', 1, false);


--
-- TOC entry 3471 (class 0 OID 0)
-- Dependencies: 268
-- Name: employee_allocation_id_employee_allocation_seq; Type: SEQUENCE SET; Schema: operations; Owner: -
--

SELECT pg_catalog.setval('operations.employee_allocation_id_employee_allocation_seq', 1, false);


--
-- TOC entry 3472 (class 0 OID 0)
-- Dependencies: 234
-- Name: projects_id_project_seq; Type: SEQUENCE SET; Schema: operations; Owner: -
--

SELECT pg_catalog.setval('operations.projects_id_project_seq', 6, true);


--
-- TOC entry 3473 (class 0 OID 0)
-- Dependencies: 236
-- Name: sales_id_sale_seq; Type: SEQUENCE SET; Schema: operations; Owner: -
--

SELECT pg_catalog.setval('operations.sales_id_sale_seq', 1, false);


--
-- TOC entry 3474 (class 0 OID 0)
-- Dependencies: 238
-- Name: service_states_id_service_state_seq; Type: SEQUENCE SET; Schema: operations; Owner: -
--

SELECT pg_catalog.setval('operations.service_states_id_service_state_seq', 1, false);


--
-- TOC entry 3475 (class 0 OID 0)
-- Dependencies: 240
-- Name: service_templates_id_service_template_seq; Type: SEQUENCE SET; Schema: operations; Owner: -
--

SELECT pg_catalog.setval('operations.service_templates_id_service_template_seq', 1, false);


--
-- TOC entry 3476 (class 0 OID 0)
-- Dependencies: 242
-- Name: services_id_service_seq; Type: SEQUENCE SET; Schema: operations; Owner: -
--

SELECT pg_catalog.setval('operations.services_id_service_seq', 1, false);


--
-- TOC entry 3477 (class 0 OID 0)
-- Dependencies: 244
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- TOC entry 3478 (class 0 OID 0)
-- Dependencies: 246
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 3479 (class 0 OID 0)
-- Dependencies: 248
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 32, true);


--
-- TOC entry 3480 (class 0 OID 0)
-- Dependencies: 251
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- TOC entry 3481 (class 0 OID 0)
-- Dependencies: 252
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 2, true);


--
-- TOC entry 3482 (class 0 OID 0)
-- Dependencies: 254
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 3483 (class 0 OID 0)
-- Dependencies: 256
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, true);


--
-- TOC entry 3484 (class 0 OID 0)
-- Dependencies: 258
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 8, true);


--
-- TOC entry 3485 (class 0 OID 0)
-- Dependencies: 260
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 21, true);


--
-- TOC entry 3486 (class 0 OID 0)
-- Dependencies: 263
-- Name: sys_rec_states_id_sys_rec_status_seq; Type: SEQUENCE SET; Schema: sys; Owner: -
--

SELECT pg_catalog.setval('sys.sys_rec_states_id_sys_rec_status_seq', 4, true);


--
-- TOC entry 3487 (class 0 OID 0)
-- Dependencies: 265
-- Name: units_id_unit_seq; Type: SEQUENCE SET; Schema: sys; Owner: -
--

SELECT pg_catalog.setval('sys.units_id_unit_seq', 21, true);


--
-- TOC entry 3097 (class 2606 OID 16634)
-- Name: asset_absence_codes asset_absence_code_pk; Type: CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_absence_codes
    ADD CONSTRAINT asset_absence_code_pk PRIMARY KEY (id_asset_absence_code);


--
-- TOC entry 3101 (class 2606 OID 16636)
-- Name: asset_absences asset_absences_pk; Type: CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_absences
    ADD CONSTRAINT asset_absences_pk PRIMARY KEY (id_asset_absence);


--
-- TOC entry 3103 (class 2606 OID 16638)
-- Name: asset_types asset_types_pk; Type: CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_types
    ADD CONSTRAINT asset_types_pk PRIMARY KEY (id_asset_type);


--
-- TOC entry 3105 (class 2606 OID 16640)
-- Name: assets assets_pk; Type: CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.assets
    ADD CONSTRAINT assets_pk PRIMARY KEY (id_asset);


--
-- TOC entry 3108 (class 2606 OID 16642)
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- TOC entry 3110 (class 2606 OID 16644)
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- TOC entry 3095 (class 2606 OID 16646)
-- Name: employee_absence_codes employee_absence_code_pk; Type: CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_absence_codes
    ADD CONSTRAINT employee_absence_code_pk PRIMARY KEY (id_employee_absence_code);


--
-- TOC entry 3099 (class 2606 OID 16648)
-- Name: employee_absences employee_absences_pk; Type: CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_absences
    ADD CONSTRAINT employee_absences_pk PRIMARY KEY (id_employee_absence);


--
-- TOC entry 3112 (class 2606 OID 16650)
-- Name: employees employee_pk; Type: CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employees
    ADD CONSTRAINT employee_pk PRIMARY KEY (id_employee);


--
-- TOC entry 3116 (class 2606 OID 16652)
-- Name: employee_types employee_type_pk; Type: CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_types
    ADD CONSTRAINT employee_type_pk PRIMARY KEY (id_employee_type);


--
-- TOC entry 3114 (class 2606 OID 16654)
-- Name: employees employee_un; Type: CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employees
    ADD CONSTRAINT employee_un UNIQUE (employee_internal_alias);


--
-- TOC entry 3118 (class 2606 OID 16656)
-- Name: currencies curency_pk; Type: CONSTRAINT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.currencies
    ADD CONSTRAINT curency_pk PRIMARY KEY (id_currency);


--
-- TOC entry 3120 (class 2606 OID 16658)
-- Name: invoice_texts customer_invoice_text_pk; Type: CONSTRAINT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.invoice_texts
    ADD CONSTRAINT customer_invoice_text_pk PRIMARY KEY (id_invoice_text);


--
-- TOC entry 3124 (class 2606 OID 16660)
-- Name: invoice_states invoice_status_pk; Type: CONSTRAINT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.invoice_states
    ADD CONSTRAINT invoice_status_pk PRIMARY KEY (id_invoice_state);


--
-- TOC entry 3122 (class 2606 OID 16662)
-- Name: invoices invoices_pk; Type: CONSTRAINT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.invoices
    ADD CONSTRAINT invoices_pk PRIMARY KEY (id_invoice);


--
-- TOC entry 3126 (class 2606 OID 16664)
-- Name: payment_conditions payment_conditions_pk; Type: CONSTRAINT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.payment_conditions
    ADD CONSTRAINT payment_conditions_pk PRIMARY KEY (id_payment_condition);


--
-- TOC entry 3128 (class 2606 OID 16666)
-- Name: companies newtable_pk; Type: CONSTRAINT; Schema: master; Owner: -
--

ALTER TABLE ONLY master.companies
    ADD CONSTRAINT newtable_pk PRIMARY KEY (id_company);


--
-- TOC entry 3130 (class 2606 OID 16668)
-- Name: companies newtable_un; Type: CONSTRAINT; Schema: master; Owner: -
--

ALTER TABLE ONLY master.companies
    ADD CONSTRAINT newtable_un UNIQUE (company_internal_alias);


--
-- TOC entry 3193 (class 2606 OID 16915)
-- Name: asset_allocation asset_allocation_pk; Type: CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.asset_allocation
    ADD CONSTRAINT asset_allocation_pk PRIMARY KEY (id_asset_allocation);


--
-- TOC entry 3195 (class 2606 OID 16917)
-- Name: asset_allocation asset_allocation_un; Type: CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.asset_allocation
    ADD CONSTRAINT asset_allocation_un UNIQUE (fk_asset, fk_task);


--
-- TOC entry 3197 (class 2606 OID 16935)
-- Name: employee_allocation employee_allocation_pk; Type: CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.employee_allocation
    ADD CONSTRAINT employee_allocation_pk PRIMARY KEY (id_employee_allocation);


--
-- TOC entry 3132 (class 2606 OID 16670)
-- Name: projects projects_pk; Type: CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.projects
    ADD CONSTRAINT projects_pk PRIMARY KEY (id_project);


--
-- TOC entry 3134 (class 2606 OID 16672)
-- Name: sales sales_pk; Type: CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.sales
    ADD CONSTRAINT sales_pk PRIMARY KEY (id_sale);


--
-- TOC entry 3136 (class 2606 OID 16674)
-- Name: task_states service_states_pk; Type: CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.task_states
    ADD CONSTRAINT service_states_pk PRIMARY KEY (id_task_state);


--
-- TOC entry 3138 (class 2606 OID 16676)
-- Name: task_templates service_templates_pk; Type: CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.task_templates
    ADD CONSTRAINT service_templates_pk PRIMARY KEY (id_task_template);


--
-- TOC entry 3140 (class 2606 OID 16678)
-- Name: tasks services_pk; Type: CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.tasks
    ADD CONSTRAINT services_pk PRIMARY KEY (id_task);


--
-- TOC entry 3143 (class 2606 OID 16680)
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 3148 (class 2606 OID 16682)
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- TOC entry 3151 (class 2606 OID 16684)
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3145 (class 2606 OID 16686)
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 3154 (class 2606 OID 16688)
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- TOC entry 3156 (class 2606 OID 16690)
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 3164 (class 2606 OID 16692)
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 3167 (class 2606 OID 16694)
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- TOC entry 3158 (class 2606 OID 16696)
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- TOC entry 3170 (class 2606 OID 16698)
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3173 (class 2606 OID 16700)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- TOC entry 3161 (class 2606 OID 16702)
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- TOC entry 3176 (class 2606 OID 16704)
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 3179 (class 2606 OID 16706)
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- TOC entry 3181 (class 2606 OID 16708)
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 3183 (class 2606 OID 16710)
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 3186 (class 2606 OID 16712)
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 3189 (class 2606 OID 16714)
-- Name: sys_rec_states sys_rec_states_pk; Type: CONSTRAINT; Schema: sys; Owner: -
--

ALTER TABLE ONLY sys.sys_rec_states
    ADD CONSTRAINT sys_rec_states_pk PRIMARY KEY (id_sys_rec_status);


--
-- TOC entry 3191 (class 2606 OID 16716)
-- Name: units units_pk; Type: CONSTRAINT; Schema: sys; Owner: -
--

ALTER TABLE ONLY sys.units
    ADD CONSTRAINT units_pk PRIMARY KEY (id_unit);


--
-- TOC entry 3106 (class 1259 OID 16717)
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: assets; Owner: -
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON assets.authtoken_token USING btree (key varchar_pattern_ops);


--
-- TOC entry 3141 (class 1259 OID 16718)
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 3146 (class 1259 OID 16719)
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- TOC entry 3149 (class 1259 OID 16720)
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- TOC entry 3152 (class 1259 OID 16721)
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- TOC entry 3162 (class 1259 OID 16722)
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- TOC entry 3165 (class 1259 OID 16723)
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- TOC entry 3168 (class 1259 OID 16724)
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- TOC entry 3171 (class 1259 OID 16725)
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- TOC entry 3159 (class 1259 OID 16726)
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- TOC entry 3174 (class 1259 OID 16727)
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- TOC entry 3177 (class 1259 OID 16728)
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- TOC entry 3184 (class 1259 OID 16729)
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- TOC entry 3187 (class 1259 OID 16730)
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 3236 (class 2620 OID 16731)
-- Name: companies default_project; Type: TRIGGER; Schema: master; Owner: -
--

CREATE TRIGGER default_project AFTER INSERT OR DELETE OR UPDATE ON master.companies FOR EACH ROW EXECUTE FUNCTION public.f_create_default_project();


--
-- TOC entry 3200 (class 2606 OID 16732)
-- Name: asset_absences asset_absences_fk; Type: FK CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_absences
    ADD CONSTRAINT asset_absences_fk FOREIGN KEY (fk_asset_absence_code) REFERENCES assets.asset_absence_codes(id_asset_absence_code);


--
-- TOC entry 3201 (class 2606 OID 16737)
-- Name: asset_absences asset_absences_fk_1; Type: FK CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_absences
    ADD CONSTRAINT asset_absences_fk_1 FOREIGN KEY (fk_asset) REFERENCES assets.assets(id_asset);


--
-- TOC entry 3202 (class 2606 OID 16742)
-- Name: assets assets_fk; Type: FK CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.assets
    ADD CONSTRAINT assets_fk FOREIGN KEY (fk_asset_type) REFERENCES assets.asset_types(id_asset_type);


--
-- TOC entry 3203 (class 2606 OID 16747)
-- Name: assets assets_rec_status; Type: FK CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.assets
    ADD CONSTRAINT assets_rec_status FOREIGN KEY (fk_sys_rec_state) REFERENCES sys.sys_rec_states(id_sys_rec_status);


--
-- TOC entry 3204 (class 2606 OID 16752)
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_auth_user_id; Type: FK CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3198 (class 2606 OID 16757)
-- Name: employee_absences employee_absence_fk; Type: FK CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_absences
    ADD CONSTRAINT employee_absence_fk FOREIGN KEY (fk_employee_absence_code) REFERENCES employees.employee_absence_codes(id_employee_absence_code);


--
-- TOC entry 3199 (class 2606 OID 16762)
-- Name: employee_absences employee_absence_fk_1; Type: FK CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_absences
    ADD CONSTRAINT employee_absence_fk_1 FOREIGN KEY (fk_employee) REFERENCES employees.employees(id_employee);


--
-- TOC entry 3205 (class 2606 OID 16767)
-- Name: employees employees_fk; Type: FK CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employees
    ADD CONSTRAINT employees_fk FOREIGN KEY (fk_sys_rec_status) REFERENCES sys.sys_rec_states(id_sys_rec_status);


--
-- TOC entry 3206 (class 2606 OID 16772)
-- Name: employees fk_employee_type; Type: FK CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employees
    ADD CONSTRAINT fk_employee_type FOREIGN KEY (fk_employee_type) REFERENCES employees.employee_types(id_employee_type);


--
-- TOC entry 3207 (class 2606 OID 16777)
-- Name: invoice_texts customer_invoice_text_fk; Type: FK CONSTRAINT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.invoice_texts
    ADD CONSTRAINT customer_invoice_text_fk FOREIGN KEY (fk_customer) REFERENCES master.companies(id_company);


--
-- TOC entry 3208 (class 2606 OID 16782)
-- Name: invoices invoices_fk; Type: FK CONSTRAINT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.invoices
    ADD CONSTRAINT invoices_fk FOREIGN KEY (fk_payment_conditions) REFERENCES finances.payment_conditions(id_payment_condition);


--
-- TOC entry 3209 (class 2606 OID 16787)
-- Name: invoices invoices_fk_1; Type: FK CONSTRAINT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.invoices
    ADD CONSTRAINT invoices_fk_1 FOREIGN KEY (fk_invoice_text) REFERENCES finances.invoice_texts(id_invoice_text);


--
-- TOC entry 3210 (class 2606 OID 16792)
-- Name: invoices invoices_fk_2; Type: FK CONSTRAINT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.invoices
    ADD CONSTRAINT invoices_fk_2 FOREIGN KEY (fk_invoice_state) REFERENCES finances.invoice_states(id_invoice_state);


--
-- TOC entry 3211 (class 2606 OID 16797)
-- Name: payment_conditions payment_conditions_fk; Type: FK CONSTRAINT; Schema: finances; Owner: -
--

ALTER TABLE ONLY finances.payment_conditions
    ADD CONSTRAINT payment_conditions_fk FOREIGN KEY (fk_currency) REFERENCES finances.currencies(id_currency);


--
-- TOC entry 3212 (class 2606 OID 16903)
-- Name: companies companies_fk; Type: FK CONSTRAINT; Schema: master; Owner: -
--

ALTER TABLE ONLY master.companies
    ADD CONSTRAINT companies_fk FOREIGN KEY (fk_sys_rec_status) REFERENCES sys.sys_rec_states(id_sys_rec_status);


--
-- TOC entry 3232 (class 2606 OID 16918)
-- Name: asset_allocation asset_allocation_fk; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.asset_allocation
    ADD CONSTRAINT asset_allocation_fk FOREIGN KEY (fk_task) REFERENCES operations.tasks(id_task);


--
-- TOC entry 3233 (class 2606 OID 16923)
-- Name: asset_allocation asset_allocation_fk_1; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.asset_allocation
    ADD CONSTRAINT asset_allocation_fk_1 FOREIGN KEY (fk_asset) REFERENCES assets.assets(id_asset);


--
-- TOC entry 3234 (class 2606 OID 16936)
-- Name: employee_allocation employee_allocation_fk; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.employee_allocation
    ADD CONSTRAINT employee_allocation_fk FOREIGN KEY (fk_employee) REFERENCES employees.employees(id_employee);


--
-- TOC entry 3235 (class 2606 OID 16941)
-- Name: employee_allocation employee_allocation_fk_1; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.employee_allocation
    ADD CONSTRAINT employee_allocation_fk_1 FOREIGN KEY (fk_task) REFERENCES operations.tasks(id_task);


--
-- TOC entry 3213 (class 2606 OID 16807)
-- Name: projects projects_fk; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.projects
    ADD CONSTRAINT projects_fk FOREIGN KEY (fk_customer) REFERENCES master.companies(id_company);


--
-- TOC entry 3214 (class 2606 OID 16812)
-- Name: sales sales_fk; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.sales
    ADD CONSTRAINT sales_fk FOREIGN KEY (fk_project) REFERENCES operations.projects(id_project);


--
-- TOC entry 3215 (class 2606 OID 16817)
-- Name: sales sales_fk3; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.sales
    ADD CONSTRAINT sales_fk3 FOREIGN KEY (fk_invoice) REFERENCES finances.invoices(id_invoice);


--
-- TOC entry 3216 (class 2606 OID 16822)
-- Name: sales sales_fk_2; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.sales
    ADD CONSTRAINT sales_fk_2 FOREIGN KEY (fk_unit) REFERENCES sys.units(id_unit);


--
-- TOC entry 3219 (class 2606 OID 16827)
-- Name: tasks service_state; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.tasks
    ADD CONSTRAINT service_state FOREIGN KEY (fk_task_state) REFERENCES operations.task_states(id_task_state);


--
-- TOC entry 3217 (class 2606 OID 16832)
-- Name: task_templates service_templates_customer; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.task_templates
    ADD CONSTRAINT service_templates_customer FOREIGN KEY (fk_customer) REFERENCES master.companies(id_company);


--
-- TOC entry 3218 (class 2606 OID 16837)
-- Name: task_templates service_templates_fk_1; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.task_templates
    ADD CONSTRAINT service_templates_fk_1 FOREIGN KEY (fk_unit) REFERENCES sys.units(id_unit);


--
-- TOC entry 3220 (class 2606 OID 16842)
-- Name: tasks services_fk; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.tasks
    ADD CONSTRAINT services_fk FOREIGN KEY (fk_unit) REFERENCES sys.units(id_unit);


--
-- TOC entry 3221 (class 2606 OID 16847)
-- Name: tasks services_fk3; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.tasks
    ADD CONSTRAINT services_fk3 FOREIGN KEY (fk_invoice) REFERENCES finances.invoices(id_invoice);


--
-- TOC entry 3222 (class 2606 OID 16852)
-- Name: tasks tasks_fk; Type: FK CONSTRAINT; Schema: operations; Owner: -
--

ALTER TABLE ONLY operations.tasks
    ADD CONSTRAINT tasks_fk FOREIGN KEY (fk_project) REFERENCES operations.projects(id_project);


--
-- TOC entry 3223 (class 2606 OID 16857)
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3224 (class 2606 OID 16862)
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3225 (class 2606 OID 16867)
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3226 (class 2606 OID 16872)
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3227 (class 2606 OID 16877)
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3228 (class 2606 OID 16882)
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3229 (class 2606 OID 16887)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3230 (class 2606 OID 16892)
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3231 (class 2606 OID 16897)
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2023-09-04 18:03:03 CEST

--
-- PostgreSQL database dump complete
--

