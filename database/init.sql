--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)

-- Started on 2023-07-31 21:22:52 CEST

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
-- TOC entry 6 (class 2615 OID 32770)
-- Name: assets; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA assets;


--
-- TOC entry 10 (class 2615 OID 16390)
-- Name: customers; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA customers;


--
-- TOC entry 11 (class 2615 OID 16385)
-- Name: employees; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA employees;


--
-- TOC entry 7 (class 2615 OID 16387)
-- Name: finance; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA finance;


--
-- TOC entry 4 (class 2615 OID 16389)
-- Name: sales; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA sales;


--
-- TOC entry 5 (class 2615 OID 16388)
-- Name: services; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA services;


--
-- TOC entry 12 (class 2615 OID 32769)
-- Name: subcontractor; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA subcontractor;


--
-- TOC entry 3 (class 2615 OID 2200)
-- Name: sys; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA sys;


--
-- TOC entry 3312 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA sys; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA sys IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 212 (class 1259 OID 16437)
-- Name: employee_absence_codes; Type: TABLE; Schema: employees; Owner: -
--

CREATE TABLE employees.employee_absence_codes (
    id_employee_absence_code integer NOT NULL,
    employee_absence_code character varying NOT NULL,
    employee_absence_code_abbreviation character varying NOT NULL
);


--
-- TOC entry 211 (class 1259 OID 16435)
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
-- TOC entry 3313 (class 0 OID 0)
-- Dependencies: 211
-- Name: employee_absence_code_id_employee_absence_code_seq; Type: SEQUENCE OWNED BY; Schema: employees; Owner: -
--

ALTER SEQUENCE employees.employee_absence_code_id_employee_absence_code_seq OWNED BY employees.employee_absence_codes.id_employee_absence_code;


--
-- TOC entry 238 (class 1259 OID 32919)
-- Name: asset_absence_codes; Type: TABLE; Schema: assets; Owner: -
--

CREATE TABLE assets.asset_absence_codes (
    id_asset_absence_code integer DEFAULT nextval('employees.employee_absence_code_id_employee_absence_code_seq'::regclass) NOT NULL,
    asset_absence_code character varying NOT NULL,
    asset_absence_code_abbreviation character varying NOT NULL
);


--
-- TOC entry 214 (class 1259 OID 16450)
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
-- TOC entry 213 (class 1259 OID 16448)
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
-- TOC entry 3314 (class 0 OID 0)
-- Dependencies: 213
-- Name: employee_absence_id_employee_absence_seq; Type: SEQUENCE OWNED BY; Schema: employees; Owner: -
--

ALTER SEQUENCE employees.employee_absence_id_employee_absence_seq OWNED BY employees.employee_absences.id_employee_absence;


--
-- TOC entry 239 (class 1259 OID 32928)
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
-- TOC entry 241 (class 1259 OID 32948)
-- Name: asset_allocation; Type: TABLE; Schema: assets; Owner: -
--

CREATE TABLE assets.asset_allocation (
    id_asset_allocation integer NOT NULL,
    date date NOT NULL,
    fk_asset integer NOT NULL,
    fk_employee integer NOT NULL,
    fk_customer integer NOT NULL
);


--
-- TOC entry 240 (class 1259 OID 32946)
-- Name: asset_allocation_id_asset_allocation_seq; Type: SEQUENCE; Schema: assets; Owner: -
--

CREATE SEQUENCE assets.asset_allocation_id_asset_allocation_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3315 (class 0 OID 0)
-- Dependencies: 240
-- Name: asset_allocation_id_asset_allocation_seq; Type: SEQUENCE OWNED BY; Schema: assets; Owner: -
--

ALTER SEQUENCE assets.asset_allocation_id_asset_allocation_seq OWNED BY assets.asset_allocation.id_asset_allocation;


--
-- TOC entry 237 (class 1259 OID 32895)
-- Name: asset_types; Type: TABLE; Schema: assets; Owner: -
--

CREATE TABLE assets.asset_types (
    id_asset_type integer NOT NULL,
    asset_type character varying NOT NULL,
    max_capacity numeric
);


--
-- TOC entry 236 (class 1259 OID 32893)
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
-- TOC entry 3316 (class 0 OID 0)
-- Dependencies: 236
-- Name: asset_types_id_asset_type_seq; Type: SEQUENCE OWNED BY; Schema: assets; Owner: -
--

ALTER SEQUENCE assets.asset_types_id_asset_type_seq OWNED BY assets.asset_types.id_asset_type;


--
-- TOC entry 234 (class 1259 OID 32879)
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
-- TOC entry 235 (class 1259 OID 32882)
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
-- TOC entry 3317 (class 0 OID 0)
-- Dependencies: 235
-- Name: assets_id_asset_seq; Type: SEQUENCE OWNED BY; Schema: assets; Owner: -
--

ALTER SEQUENCE assets.assets_id_asset_seq OWNED BY assets.assets.id_asset;


--
-- TOC entry 216 (class 1259 OID 16472)
-- Name: customers; Type: TABLE; Schema: customers; Owner: -
--

CREATE TABLE customers.customers (
    id_customer integer NOT NULL,
    customer_company_name character varying,
    customer_street character varying NOT NULL,
    customer_zipcode character varying NOT NULL,
    customer_country character varying NOT NULL,
    customer_city character varying NOT NULL,
    customer_internal_alias character varying NOT NULL,
    fk_sys_rec_status integer NOT NULL,
    customer_email character varying
);


--
-- TOC entry 215 (class 1259 OID 16470)
-- Name: newtable_id_customer_seq; Type: SEQUENCE; Schema: customers; Owner: -
--

CREATE SEQUENCE customers.newtable_id_customer_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3318 (class 0 OID 0)
-- Dependencies: 215
-- Name: newtable_id_customer_seq; Type: SEQUENCE OWNED BY; Schema: customers; Owner: -
--

ALTER SEQUENCE customers.newtable_id_customer_seq OWNED BY customers.customers.id_customer;


--
-- TOC entry 208 (class 1259 OID 16393)
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
-- TOC entry 207 (class 1259 OID 16391)
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
-- TOC entry 3319 (class 0 OID 0)
-- Dependencies: 207
-- Name: employee_id_employee_seq; Type: SEQUENCE OWNED BY; Schema: employees; Owner: -
--

ALTER SEQUENCE employees.employee_id_employee_seq OWNED BY employees.employees.id_employee;


--
-- TOC entry 210 (class 1259 OID 16404)
-- Name: employee_types; Type: TABLE; Schema: employees; Owner: -
--

CREATE TABLE employees.employee_types (
    id_employee_type integer NOT NULL,
    employee_type_description character varying NOT NULL
);


--
-- TOC entry 209 (class 1259 OID 16402)
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
-- TOC entry 3320 (class 0 OID 0)
-- Dependencies: 209
-- Name: employee_type_employee_type_seq; Type: SEQUENCE OWNED BY; Schema: employees; Owner: -
--

ALTER SEQUENCE employees.employee_type_employee_type_seq OWNED BY employees.employee_types.id_employee_type;


--
-- TOC entry 220 (class 1259 OID 16515)
-- Name: currencies; Type: TABLE; Schema: finance; Owner: -
--

CREATE TABLE finance.currencies (
    id_currency integer NOT NULL,
    currency character varying NOT NULL,
    currency_abbreviation character varying NOT NULL,
    currency_account_nr character varying NOT NULL
);


--
-- TOC entry 219 (class 1259 OID 16513)
-- Name: curency_id_currency_seq; Type: SEQUENCE; Schema: finance; Owner: -
--

CREATE SEQUENCE finance.curency_id_currency_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3321 (class 0 OID 0)
-- Dependencies: 219
-- Name: curency_id_currency_seq; Type: SEQUENCE OWNED BY; Schema: finance; Owner: -
--

ALTER SEQUENCE finance.curency_id_currency_seq OWNED BY finance.currencies.id_currency;


--
-- TOC entry 218 (class 1259 OID 16501)
-- Name: invoice_texts; Type: TABLE; Schema: finance; Owner: -
--

CREATE TABLE finance.invoice_texts (
    id_invoice_text integer NOT NULL,
    invoice_text character varying NOT NULL,
    fk_customer integer NOT NULL
);


--
-- TOC entry 217 (class 1259 OID 16499)
-- Name: customer_invoice_text_id_customer_invoice_text_seq; Type: SEQUENCE; Schema: finance; Owner: -
--

CREATE SEQUENCE finance.customer_invoice_text_id_customer_invoice_text_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3322 (class 0 OID 0)
-- Dependencies: 217
-- Name: customer_invoice_text_id_customer_invoice_text_seq; Type: SEQUENCE OWNED BY; Schema: finance; Owner: -
--

ALTER SEQUENCE finance.customer_invoice_text_id_customer_invoice_text_seq OWNED BY finance.invoice_texts.id_invoice_text;


--
-- TOC entry 226 (class 1259 OID 24590)
-- Name: sales_invoices; Type: TABLE; Schema: finance; Owner: -
--

CREATE TABLE finance.sales_invoices (
    id_sales_invoice integer NOT NULL,
    invoice_date date,
    fk_invoice_text integer,
    fk_invoice_state integer NOT NULL,
    fk_payment_conditions integer NOT NULL
);


--
-- TOC entry 225 (class 1259 OID 24588)
-- Name: invoice_id_invoice_seq; Type: SEQUENCE; Schema: finance; Owner: -
--

CREATE SEQUENCE finance.invoice_id_invoice_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3323 (class 0 OID 0)
-- Dependencies: 225
-- Name: invoice_id_invoice_seq; Type: SEQUENCE OWNED BY; Schema: finance; Owner: -
--

ALTER SEQUENCE finance.invoice_id_invoice_seq OWNED BY finance.sales_invoices.id_sales_invoice;


--
-- TOC entry 224 (class 1259 OID 24579)
-- Name: invoice_states; Type: TABLE; Schema: finance; Owner: -
--

CREATE TABLE finance.invoice_states (
    id_invoice_state integer NOT NULL,
    invoice_state character varying NOT NULL,
    invoice_state_abbreviation integer NOT NULL
);


--
-- TOC entry 223 (class 1259 OID 24577)
-- Name: invoice_status_id_invoice_status_seq; Type: SEQUENCE; Schema: finance; Owner: -
--

CREATE SEQUENCE finance.invoice_status_id_invoice_status_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3324 (class 0 OID 0)
-- Dependencies: 223
-- Name: invoice_status_id_invoice_status_seq; Type: SEQUENCE OWNED BY; Schema: finance; Owner: -
--

ALTER SEQUENCE finance.invoice_status_id_invoice_status_seq OWNED BY finance.invoice_states.id_invoice_state;


--
-- TOC entry 232 (class 1259 OID 32810)
-- Name: payment_conditions; Type: TABLE; Schema: finance; Owner: -
--

CREATE TABLE finance.payment_conditions (
    id_payment_condition integer NOT NULL,
    vat numeric NOT NULL,
    fk_currency integer NOT NULL,
    due_days integer NOT NULL
);


--
-- TOC entry 231 (class 1259 OID 32808)
-- Name: payment_conditions_id_payment_condition_seq; Type: SEQUENCE; Schema: finance; Owner: -
--

CREATE SEQUENCE finance.payment_conditions_id_payment_condition_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3325 (class 0 OID 0)
-- Dependencies: 231
-- Name: payment_conditions_id_payment_condition_seq; Type: SEQUENCE OWNED BY; Schema: finance; Owner: -
--

ALTER SEQUENCE finance.payment_conditions_id_payment_condition_seq OWNED BY finance.payment_conditions.id_payment_condition;


--
-- TOC entry 233 (class 1259 OID 32845)
-- Name: service_invoices; Type: TABLE; Schema: finance; Owner: -
--

CREATE TABLE finance.service_invoices (
    id_service_invoice integer DEFAULT nextval('finance.invoice_id_invoice_seq'::regclass) NOT NULL,
    invoice_date date,
    fk_invoice_text integer,
    fk_invoice_state integer NOT NULL,
    fk_payment_condition integer NOT NULL
);


--
-- TOC entry 228 (class 1259 OID 32773)
-- Name: products; Type: TABLE; Schema: sales; Owner: -
--

CREATE TABLE sales.products (
    id_product integer NOT NULL,
    product_name character varying NOT NULL,
    fk_unit integer NOT NULL
);


--
-- TOC entry 227 (class 1259 OID 32771)
-- Name: product_id_product_seq; Type: SEQUENCE; Schema: sales; Owner: -
--

CREATE SEQUENCE sales.product_id_product_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3326 (class 0 OID 0)
-- Dependencies: 227
-- Name: product_id_product_seq; Type: SEQUENCE OWNED BY; Schema: sales; Owner: -
--

ALTER SEQUENCE sales.product_id_product_seq OWNED BY sales.products.id_product;


--
-- TOC entry 222 (class 1259 OID 16539)
-- Name: sales; Type: TABLE; Schema: sales; Owner: -
--

CREATE TABLE sales.sales (
    id_sale integer NOT NULL,
    sale_timestamp timestamp without time zone NOT NULL,
    fk_customer integer NOT NULL,
    sale_amount numeric NOT NULL,
    sale_unit_price numeric NOT NULL,
    sales_reference character varying NOT NULL,
    fk_unit integer NOT NULL,
    fk_product integer NOT NULL,
    fk_invoice integer NOT NULL
);


--
-- TOC entry 221 (class 1259 OID 16537)
-- Name: sales_id_sale_seq; Type: SEQUENCE; Schema: sales; Owner: -
--

CREATE SEQUENCE sales.sales_id_sale_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3327 (class 0 OID 0)
-- Dependencies: 221
-- Name: sales_id_sale_seq; Type: SEQUENCE OWNED BY; Schema: sales; Owner: -
--

ALTER SEQUENCE sales.sales_id_sale_seq OWNED BY sales.sales.id_sale;


--
-- TOC entry 245 (class 1259 OID 32984)
-- Name: service_states; Type: TABLE; Schema: services; Owner: -
--

CREATE TABLE services.service_states (
    id_service_state integer NOT NULL,
    service_state character varying NOT NULL
);


--
-- TOC entry 244 (class 1259 OID 32982)
-- Name: service_states_id_service_state_seq; Type: SEQUENCE; Schema: services; Owner: -
--

CREATE SEQUENCE services.service_states_id_service_state_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3328 (class 0 OID 0)
-- Dependencies: 244
-- Name: service_states_id_service_state_seq; Type: SEQUENCE OWNED BY; Schema: services; Owner: -
--

ALTER SEQUENCE services.service_states_id_service_state_seq OWNED BY services.service_states.id_service_state;


--
-- TOC entry 251 (class 1259 OID 33057)
-- Name: service_templates; Type: TABLE; Schema: services; Owner: -
--

CREATE TABLE services.service_templates (
    id_service_template integer NOT NULL,
    fk_customer integer NOT NULL,
    fk_unit integer NOT NULL,
    service_amount numeric NOT NULL,
    service_unit_price numeric NOT NULL,
    service_description character varying NOT NULL,
    fk_service_type integer NOT NULL
);


--
-- TOC entry 250 (class 1259 OID 33055)
-- Name: service_templates_id_service_template_seq; Type: SEQUENCE; Schema: services; Owner: -
--

CREATE SEQUENCE services.service_templates_id_service_template_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3329 (class 0 OID 0)
-- Dependencies: 250
-- Name: service_templates_id_service_template_seq; Type: SEQUENCE OWNED BY; Schema: services; Owner: -
--

ALTER SEQUENCE services.service_templates_id_service_template_seq OWNED BY services.service_templates.id_service_template;


--
-- TOC entry 247 (class 1259 OID 32994)
-- Name: service_types; Type: TABLE; Schema: services; Owner: -
--

CREATE TABLE services.service_types (
    id_service_type integer NOT NULL,
    service_type character varying NOT NULL
);


--
-- TOC entry 246 (class 1259 OID 32992)
-- Name: service_types_id_service_type_seq; Type: SEQUENCE; Schema: services; Owner: -
--

CREATE SEQUENCE services.service_types_id_service_type_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3330 (class 0 OID 0)
-- Dependencies: 246
-- Name: service_types_id_service_type_seq; Type: SEQUENCE OWNED BY; Schema: services; Owner: -
--

ALTER SEQUENCE services.service_types_id_service_type_seq OWNED BY services.service_types.id_service_type;


--
-- TOC entry 243 (class 1259 OID 32975)
-- Name: services; Type: TABLE; Schema: services; Owner: -
--

CREATE TABLE services.services (
    id_service integer NOT NULL,
    fk_customer integer NOT NULL,
    fk_service_state integer NOT NULL,
    timestamp_from timestamp without time zone,
    timestamp_to timestamp without time zone,
    amount numeric,
    unit_price numeric,
    service_description character varying NOT NULL,
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
-- TOC entry 242 (class 1259 OID 32973)
-- Name: services_id_service_seq; Type: SEQUENCE; Schema: services; Owner: -
--

CREATE SEQUENCE services.services_id_service_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3331 (class 0 OID 0)
-- Dependencies: 242
-- Name: services_id_service_seq; Type: SEQUENCE OWNED BY; Schema: services; Owner: -
--

ALTER SEQUENCE services.services_id_service_seq OWNED BY services.services.id_service;


--
-- TOC entry 253 (class 1259 OID 33083)
-- Name: subcontractors; Type: TABLE; Schema: subcontractor; Owner: -
--

CREATE TABLE subcontractor.subcontractors (
    id_subcontractor integer NOT NULL,
    subcontractor_company_name character varying NOT NULL,
    subcontractor_street character varying NOT NULL,
    subcontractor_house_nr character varying NOT NULL,
    subcontractor_zipcode character varying NOT NULL,
    subcontractor_city character varying NOT NULL,
    subcontractor_country character varying NOT NULL,
    subcontractor_email character varying NOT NULL,
    fk_sys_rec_status integer NOT NULL
);


--
-- TOC entry 252 (class 1259 OID 33081)
-- Name: subcontractors_id_subcontractor_seq; Type: SEQUENCE; Schema: subcontractor; Owner: -
--

CREATE SEQUENCE subcontractor.subcontractors_id_subcontractor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3332 (class 0 OID 0)
-- Dependencies: 252
-- Name: subcontractors_id_subcontractor_seq; Type: SEQUENCE OWNED BY; Schema: subcontractor; Owner: -
--

ALTER SEQUENCE subcontractor.subcontractors_id_subcontractor_seq OWNED BY subcontractor.subcontractors.id_subcontractor;


--
-- TOC entry 230 (class 1259 OID 32789)
-- Name: sys_rec_states; Type: TABLE; Schema: sys; Owner: -
--

CREATE TABLE sys.sys_rec_states (
    id_sys_rec_status integer NOT NULL,
    sys_rec_status character varying NOT NULL
);


--
-- TOC entry 229 (class 1259 OID 32787)
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
-- TOC entry 3333 (class 0 OID 0)
-- Dependencies: 229
-- Name: sys_rec_states_id_sys_rec_status_seq; Type: SEQUENCE OWNED BY; Schema: sys; Owner: -
--

ALTER SEQUENCE sys.sys_rec_states_id_sys_rec_status_seq OWNED BY sys.sys_rec_states.id_sys_rec_status;


--
-- TOC entry 249 (class 1259 OID 33036)
-- Name: units; Type: TABLE; Schema: sys; Owner: -
--

CREATE TABLE sys.units (
    id_unit integer NOT NULL,
    unit character varying NOT NULL,
    unit_abbreviation character varying NOT NULL
);


--
-- TOC entry 248 (class 1259 OID 33034)
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
-- TOC entry 3334 (class 0 OID 0)
-- Dependencies: 248
-- Name: units_id_unit_seq; Type: SEQUENCE OWNED BY; Schema: sys; Owner: -
--

ALTER SEQUENCE sys.units_id_unit_seq OWNED BY sys.units.id_unit;


--
-- TOC entry 3035 (class 2604 OID 32951)
-- Name: asset_allocation id_asset_allocation; Type: DEFAULT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_allocation ALTER COLUMN id_asset_allocation SET DEFAULT nextval('assets.asset_allocation_id_asset_allocation_seq'::regclass);


--
-- TOC entry 3032 (class 2604 OID 32898)
-- Name: asset_types id_asset_type; Type: DEFAULT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_types ALTER COLUMN id_asset_type SET DEFAULT nextval('assets.asset_types_id_asset_type_seq'::regclass);


--
-- TOC entry 3031 (class 2604 OID 32884)
-- Name: assets id_asset; Type: DEFAULT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.assets ALTER COLUMN id_asset SET DEFAULT nextval('assets.assets_id_asset_seq'::regclass);


--
-- TOC entry 3021 (class 2604 OID 16475)
-- Name: customers id_customer; Type: DEFAULT; Schema: customers; Owner: -
--

ALTER TABLE ONLY customers.customers ALTER COLUMN id_customer SET DEFAULT nextval('customers.newtable_id_customer_seq'::regclass);


--
-- TOC entry 3019 (class 2604 OID 16440)
-- Name: employee_absence_codes id_employee_absence_code; Type: DEFAULT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_absence_codes ALTER COLUMN id_employee_absence_code SET DEFAULT nextval('employees.employee_absence_code_id_employee_absence_code_seq'::regclass);


--
-- TOC entry 3020 (class 2604 OID 16453)
-- Name: employee_absences id_employee_absence; Type: DEFAULT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_absences ALTER COLUMN id_employee_absence SET DEFAULT nextval('employees.employee_absence_id_employee_absence_seq'::regclass);


--
-- TOC entry 3018 (class 2604 OID 16407)
-- Name: employee_types id_employee_type; Type: DEFAULT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_types ALTER COLUMN id_employee_type SET DEFAULT nextval('employees.employee_type_employee_type_seq'::regclass);


--
-- TOC entry 3016 (class 2604 OID 16396)
-- Name: employees id_employee; Type: DEFAULT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employees ALTER COLUMN id_employee SET DEFAULT nextval('employees.employee_id_employee_seq'::regclass);


--
-- TOC entry 3023 (class 2604 OID 16518)
-- Name: currencies id_currency; Type: DEFAULT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.currencies ALTER COLUMN id_currency SET DEFAULT nextval('finance.curency_id_currency_seq'::regclass);


--
-- TOC entry 3025 (class 2604 OID 24582)
-- Name: invoice_states id_invoice_state; Type: DEFAULT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.invoice_states ALTER COLUMN id_invoice_state SET DEFAULT nextval('finance.invoice_status_id_invoice_status_seq'::regclass);


--
-- TOC entry 3022 (class 2604 OID 16504)
-- Name: invoice_texts id_invoice_text; Type: DEFAULT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.invoice_texts ALTER COLUMN id_invoice_text SET DEFAULT nextval('finance.customer_invoice_text_id_customer_invoice_text_seq'::regclass);


--
-- TOC entry 3029 (class 2604 OID 32813)
-- Name: payment_conditions id_payment_condition; Type: DEFAULT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.payment_conditions ALTER COLUMN id_payment_condition SET DEFAULT nextval('finance.payment_conditions_id_payment_condition_seq'::regclass);


--
-- TOC entry 3026 (class 2604 OID 24593)
-- Name: sales_invoices id_sales_invoice; Type: DEFAULT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.sales_invoices ALTER COLUMN id_sales_invoice SET DEFAULT nextval('finance.invoice_id_invoice_seq'::regclass);


--
-- TOC entry 3027 (class 2604 OID 32776)
-- Name: products id_product; Type: DEFAULT; Schema: sales; Owner: -
--

ALTER TABLE ONLY sales.products ALTER COLUMN id_product SET DEFAULT nextval('sales.product_id_product_seq'::regclass);


--
-- TOC entry 3024 (class 2604 OID 16542)
-- Name: sales id_sale; Type: DEFAULT; Schema: sales; Owner: -
--

ALTER TABLE ONLY sales.sales ALTER COLUMN id_sale SET DEFAULT nextval('sales.sales_id_sale_seq'::regclass);


--
-- TOC entry 3037 (class 2604 OID 32987)
-- Name: service_states id_service_state; Type: DEFAULT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.service_states ALTER COLUMN id_service_state SET DEFAULT nextval('services.service_states_id_service_state_seq'::regclass);


--
-- TOC entry 3040 (class 2604 OID 33060)
-- Name: service_templates id_service_template; Type: DEFAULT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.service_templates ALTER COLUMN id_service_template SET DEFAULT nextval('services.service_templates_id_service_template_seq'::regclass);


--
-- TOC entry 3038 (class 2604 OID 32997)
-- Name: service_types id_service_type; Type: DEFAULT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.service_types ALTER COLUMN id_service_type SET DEFAULT nextval('services.service_types_id_service_type_seq'::regclass);


--
-- TOC entry 3036 (class 2604 OID 32978)
-- Name: services id_service; Type: DEFAULT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.services ALTER COLUMN id_service SET DEFAULT nextval('services.services_id_service_seq'::regclass);


--
-- TOC entry 3041 (class 2604 OID 33086)
-- Name: subcontractors id_subcontractor; Type: DEFAULT; Schema: subcontractor; Owner: -
--

ALTER TABLE ONLY subcontractor.subcontractors ALTER COLUMN id_subcontractor SET DEFAULT nextval('subcontractor.subcontractors_id_subcontractor_seq'::regclass);


--
-- TOC entry 3028 (class 2604 OID 32792)
-- Name: sys_rec_states id_sys_rec_status; Type: DEFAULT; Schema: sys; Owner: -
--

ALTER TABLE ONLY sys.sys_rec_states ALTER COLUMN id_sys_rec_status SET DEFAULT nextval('sys.sys_rec_states_id_sys_rec_status_seq'::regclass);


--
-- TOC entry 3039 (class 2604 OID 33039)
-- Name: units id_unit; Type: DEFAULT; Schema: sys; Owner: -
--

ALTER TABLE ONLY sys.units ALTER COLUMN id_unit SET DEFAULT nextval('sys.units_id_unit_seq'::regclass);


--
-- TOC entry 3291 (class 0 OID 32919)
-- Dependencies: 238
-- Data for Name: asset_absence_codes; Type: TABLE DATA; Schema: assets; Owner: -
--

COPY assets.asset_absence_codes (id_asset_absence_code, asset_absence_code, asset_absence_code_abbreviation) FROM stdin;
\.


--
-- TOC entry 3292 (class 0 OID 32928)
-- Dependencies: 239
-- Data for Name: asset_absences; Type: TABLE DATA; Schema: assets; Owner: -
--

COPY assets.asset_absences (id_asset_absence, "from", "to", fk_asset, fk_asset_absence_code) FROM stdin;
\.


--
-- TOC entry 3294 (class 0 OID 32948)
-- Dependencies: 241
-- Data for Name: asset_allocation; Type: TABLE DATA; Schema: assets; Owner: -
--

COPY assets.asset_allocation (id_asset_allocation, date, fk_asset, fk_employee, fk_customer) FROM stdin;
\.


--
-- TOC entry 3290 (class 0 OID 32895)
-- Dependencies: 237
-- Data for Name: asset_types; Type: TABLE DATA; Schema: assets; Owner: -
--

COPY assets.asset_types (id_asset_type, asset_type, max_capacity) FROM stdin;
\.


--
-- TOC entry 3287 (class 0 OID 32879)
-- Dependencies: 234
-- Data for Name: assets; Type: TABLE DATA; Schema: assets; Owner: -
--

COPY assets.assets (id_asset, fk_asset_type, asset_description, fk_employee, asset_internal_alias, year_of_production, asset_km_counter, fk_sys_rec_state) FROM stdin;
\.


--
-- TOC entry 3269 (class 0 OID 16472)
-- Dependencies: 216
-- Data for Name: customers; Type: TABLE DATA; Schema: customers; Owner: -
--

COPY customers.customers (id_customer, customer_company_name, customer_street, customer_zipcode, customer_country, customer_city, customer_internal_alias, fk_sys_rec_status, customer_email) FROM stdin;
\.


--
-- TOC entry 3265 (class 0 OID 16437)
-- Dependencies: 212
-- Data for Name: employee_absence_codes; Type: TABLE DATA; Schema: employees; Owner: -
--

COPY employees.employee_absence_codes (id_employee_absence_code, employee_absence_code, employee_absence_code_abbreviation) FROM stdin;
\.


--
-- TOC entry 3267 (class 0 OID 16450)
-- Dependencies: 214
-- Data for Name: employee_absences; Type: TABLE DATA; Schema: employees; Owner: -
--

COPY employees.employee_absences (id_employee_absence, "from", "to", fk_employee, fk_employee_absence_code) FROM stdin;
\.


--
-- TOC entry 3263 (class 0 OID 16404)
-- Dependencies: 210
-- Data for Name: employee_types; Type: TABLE DATA; Schema: employees; Owner: -
--

COPY employees.employee_types (id_employee_type, employee_type_description) FROM stdin;
\.


--
-- TOC entry 3261 (class 0 OID 16393)
-- Dependencies: 208
-- Data for Name: employees; Type: TABLE DATA; Schema: employees; Owner: -
--

COPY employees.employees (id_employee, employee_first_name, employee_last_name, employee_street, employee_zipcode, employee_city, emplyee_email, employee_cell_phone, emplyee_birthday, emplyee_salary, fk_employee_type, employee_fte, employee_internal_alias, fk_sys_rec_status, employee_house_nr) FROM stdin;
\.


--
-- TOC entry 3273 (class 0 OID 16515)
-- Dependencies: 220
-- Data for Name: currencies; Type: TABLE DATA; Schema: finance; Owner: -
--

COPY finance.currencies (id_currency, currency, currency_abbreviation, currency_account_nr) FROM stdin;
\.


--
-- TOC entry 3277 (class 0 OID 24579)
-- Dependencies: 224
-- Data for Name: invoice_states; Type: TABLE DATA; Schema: finance; Owner: -
--

COPY finance.invoice_states (id_invoice_state, invoice_state, invoice_state_abbreviation) FROM stdin;
\.


--
-- TOC entry 3271 (class 0 OID 16501)
-- Dependencies: 218
-- Data for Name: invoice_texts; Type: TABLE DATA; Schema: finance; Owner: -
--

COPY finance.invoice_texts (id_invoice_text, invoice_text, fk_customer) FROM stdin;
\.


--
-- TOC entry 3285 (class 0 OID 32810)
-- Dependencies: 232
-- Data for Name: payment_conditions; Type: TABLE DATA; Schema: finance; Owner: -
--

COPY finance.payment_conditions (id_payment_condition, vat, fk_currency, due_days) FROM stdin;
\.


--
-- TOC entry 3279 (class 0 OID 24590)
-- Dependencies: 226
-- Data for Name: sales_invoices; Type: TABLE DATA; Schema: finance; Owner: -
--

COPY finance.sales_invoices (id_sales_invoice, invoice_date, fk_invoice_text, fk_invoice_state, fk_payment_conditions) FROM stdin;
\.


--
-- TOC entry 3286 (class 0 OID 32845)
-- Dependencies: 233
-- Data for Name: service_invoices; Type: TABLE DATA; Schema: finance; Owner: -
--

COPY finance.service_invoices (id_service_invoice, invoice_date, fk_invoice_text, fk_invoice_state, fk_payment_condition) FROM stdin;
\.


--
-- TOC entry 3281 (class 0 OID 32773)
-- Dependencies: 228
-- Data for Name: products; Type: TABLE DATA; Schema: sales; Owner: -
--

COPY sales.products (id_product, product_name, fk_unit) FROM stdin;
\.


--
-- TOC entry 3275 (class 0 OID 16539)
-- Dependencies: 222
-- Data for Name: sales; Type: TABLE DATA; Schema: sales; Owner: -
--

COPY sales.sales (id_sale, sale_timestamp, fk_customer, sale_amount, sale_unit_price, sales_reference, fk_unit, fk_product, fk_invoice) FROM stdin;
\.


--
-- TOC entry 3298 (class 0 OID 32984)
-- Dependencies: 245
-- Data for Name: service_states; Type: TABLE DATA; Schema: services; Owner: -
--

COPY services.service_states (id_service_state, service_state) FROM stdin;
\.


--
-- TOC entry 3304 (class 0 OID 33057)
-- Dependencies: 251
-- Data for Name: service_templates; Type: TABLE DATA; Schema: services; Owner: -
--

COPY services.service_templates (id_service_template, fk_customer, fk_unit, service_amount, service_unit_price, service_description, fk_service_type) FROM stdin;
\.


--
-- TOC entry 3300 (class 0 OID 32994)
-- Dependencies: 247
-- Data for Name: service_types; Type: TABLE DATA; Schema: services; Owner: -
--

COPY services.service_types (id_service_type, service_type) FROM stdin;
\.


--
-- TOC entry 3296 (class 0 OID 32975)
-- Dependencies: 243
-- Data for Name: services; Type: TABLE DATA; Schema: services; Owner: -
--

COPY services.services (id_service, fk_customer, fk_service_state, timestamp_from, timestamp_to, amount, unit_price, service_description, fk_invoice, fk_unit, fk_asset_allocation, internal_info, customer_reference, fk_subcontractor, brokerage_fee, fk_service_type) FROM stdin;
\.


--
-- TOC entry 3306 (class 0 OID 33083)
-- Dependencies: 253
-- Data for Name: subcontractors; Type: TABLE DATA; Schema: subcontractor; Owner: -
--

COPY subcontractor.subcontractors (id_subcontractor, subcontractor_company_name, subcontractor_street, subcontractor_house_nr, subcontractor_zipcode, subcontractor_city, subcontractor_country, subcontractor_email, fk_sys_rec_status) FROM stdin;
\.


--
-- TOC entry 3283 (class 0 OID 32789)
-- Dependencies: 230
-- Data for Name: sys_rec_states; Type: TABLE DATA; Schema: sys; Owner: -
--

COPY sys.sys_rec_states (id_sys_rec_status, sys_rec_status) FROM stdin;
\.


--
-- TOC entry 3302 (class 0 OID 33036)
-- Dependencies: 249
-- Data for Name: units; Type: TABLE DATA; Schema: sys; Owner: -
--

COPY sys.units (id_unit, unit, unit_abbreviation) FROM stdin;
\.


--
-- TOC entry 3335 (class 0 OID 0)
-- Dependencies: 240
-- Name: asset_allocation_id_asset_allocation_seq; Type: SEQUENCE SET; Schema: assets; Owner: -
--

SELECT pg_catalog.setval('assets.asset_allocation_id_asset_allocation_seq', 1, false);


--
-- TOC entry 3336 (class 0 OID 0)
-- Dependencies: 236
-- Name: asset_types_id_asset_type_seq; Type: SEQUENCE SET; Schema: assets; Owner: -
--

SELECT pg_catalog.setval('assets.asset_types_id_asset_type_seq', 1, false);


--
-- TOC entry 3337 (class 0 OID 0)
-- Dependencies: 235
-- Name: assets_id_asset_seq; Type: SEQUENCE SET; Schema: assets; Owner: -
--

SELECT pg_catalog.setval('assets.assets_id_asset_seq', 1, false);


--
-- TOC entry 3338 (class 0 OID 0)
-- Dependencies: 215
-- Name: newtable_id_customer_seq; Type: SEQUENCE SET; Schema: customers; Owner: -
--

SELECT pg_catalog.setval('customers.newtable_id_customer_seq', 1, false);


--
-- TOC entry 3339 (class 0 OID 0)
-- Dependencies: 211
-- Name: employee_absence_code_id_employee_absence_code_seq; Type: SEQUENCE SET; Schema: employees; Owner: -
--

SELECT pg_catalog.setval('employees.employee_absence_code_id_employee_absence_code_seq', 1, false);


--
-- TOC entry 3340 (class 0 OID 0)
-- Dependencies: 213
-- Name: employee_absence_id_employee_absence_seq; Type: SEQUENCE SET; Schema: employees; Owner: -
--

SELECT pg_catalog.setval('employees.employee_absence_id_employee_absence_seq', 1, false);


--
-- TOC entry 3341 (class 0 OID 0)
-- Dependencies: 207
-- Name: employee_id_employee_seq; Type: SEQUENCE SET; Schema: employees; Owner: -
--

SELECT pg_catalog.setval('employees.employee_id_employee_seq', 1, true);


--
-- TOC entry 3342 (class 0 OID 0)
-- Dependencies: 209
-- Name: employee_type_employee_type_seq; Type: SEQUENCE SET; Schema: employees; Owner: -
--

SELECT pg_catalog.setval('employees.employee_type_employee_type_seq', 1, false);


--
-- TOC entry 3343 (class 0 OID 0)
-- Dependencies: 219
-- Name: curency_id_currency_seq; Type: SEQUENCE SET; Schema: finance; Owner: -
--

SELECT pg_catalog.setval('finance.curency_id_currency_seq', 1, false);


--
-- TOC entry 3344 (class 0 OID 0)
-- Dependencies: 217
-- Name: customer_invoice_text_id_customer_invoice_text_seq; Type: SEQUENCE SET; Schema: finance; Owner: -
--

SELECT pg_catalog.setval('finance.customer_invoice_text_id_customer_invoice_text_seq', 1, false);


--
-- TOC entry 3345 (class 0 OID 0)
-- Dependencies: 225
-- Name: invoice_id_invoice_seq; Type: SEQUENCE SET; Schema: finance; Owner: -
--

SELECT pg_catalog.setval('finance.invoice_id_invoice_seq', 1, false);


--
-- TOC entry 3346 (class 0 OID 0)
-- Dependencies: 223
-- Name: invoice_status_id_invoice_status_seq; Type: SEQUENCE SET; Schema: finance; Owner: -
--

SELECT pg_catalog.setval('finance.invoice_status_id_invoice_status_seq', 1, false);


--
-- TOC entry 3347 (class 0 OID 0)
-- Dependencies: 231
-- Name: payment_conditions_id_payment_condition_seq; Type: SEQUENCE SET; Schema: finance; Owner: -
--

SELECT pg_catalog.setval('finance.payment_conditions_id_payment_condition_seq', 1, false);


--
-- TOC entry 3348 (class 0 OID 0)
-- Dependencies: 227
-- Name: product_id_product_seq; Type: SEQUENCE SET; Schema: sales; Owner: -
--

SELECT pg_catalog.setval('sales.product_id_product_seq', 1, false);


--
-- TOC entry 3349 (class 0 OID 0)
-- Dependencies: 221
-- Name: sales_id_sale_seq; Type: SEQUENCE SET; Schema: sales; Owner: -
--

SELECT pg_catalog.setval('sales.sales_id_sale_seq', 1, false);


--
-- TOC entry 3350 (class 0 OID 0)
-- Dependencies: 244
-- Name: service_states_id_service_state_seq; Type: SEQUENCE SET; Schema: services; Owner: -
--

SELECT pg_catalog.setval('services.service_states_id_service_state_seq', 1, false);


--
-- TOC entry 3351 (class 0 OID 0)
-- Dependencies: 250
-- Name: service_templates_id_service_template_seq; Type: SEQUENCE SET; Schema: services; Owner: -
--

SELECT pg_catalog.setval('services.service_templates_id_service_template_seq', 1, false);


--
-- TOC entry 3352 (class 0 OID 0)
-- Dependencies: 246
-- Name: service_types_id_service_type_seq; Type: SEQUENCE SET; Schema: services; Owner: -
--

SELECT pg_catalog.setval('services.service_types_id_service_type_seq', 1, false);


--
-- TOC entry 3353 (class 0 OID 0)
-- Dependencies: 242
-- Name: services_id_service_seq; Type: SEQUENCE SET; Schema: services; Owner: -
--

SELECT pg_catalog.setval('services.services_id_service_seq', 1, false);


--
-- TOC entry 3354 (class 0 OID 0)
-- Dependencies: 252
-- Name: subcontractors_id_subcontractor_seq; Type: SEQUENCE SET; Schema: subcontractor; Owner: -
--

SELECT pg_catalog.setval('subcontractor.subcontractors_id_subcontractor_seq', 1, false);


--
-- TOC entry 3355 (class 0 OID 0)
-- Dependencies: 229
-- Name: sys_rec_states_id_sys_rec_status_seq; Type: SEQUENCE SET; Schema: sys; Owner: -
--

SELECT pg_catalog.setval('sys.sys_rec_states_id_sys_rec_status_seq', 1, false);


--
-- TOC entry 3356 (class 0 OID 0)
-- Dependencies: 248
-- Name: units_id_unit_seq; Type: SEQUENCE SET; Schema: sys; Owner: -
--

SELECT pg_catalog.setval('sys.units_id_unit_seq', 1, false);


--
-- TOC entry 3077 (class 2606 OID 32927)
-- Name: asset_absence_codes asset_absence_code_pk; Type: CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_absence_codes
    ADD CONSTRAINT asset_absence_code_pk PRIMARY KEY (id_asset_absence_code);


--
-- TOC entry 3079 (class 2606 OID 32933)
-- Name: asset_absences asset_absences_pk; Type: CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_absences
    ADD CONSTRAINT asset_absences_pk PRIMARY KEY (id_asset_absence);


--
-- TOC entry 3081 (class 2606 OID 32953)
-- Name: asset_allocation asset_allocation_pk; Type: CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_allocation
    ADD CONSTRAINT asset_allocation_pk PRIMARY KEY (id_asset_allocation);


--
-- TOC entry 3083 (class 2606 OID 32955)
-- Name: asset_allocation asset_allocation_un; Type: CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_allocation
    ADD CONSTRAINT asset_allocation_un UNIQUE (date, fk_asset);


--
-- TOC entry 3075 (class 2606 OID 32903)
-- Name: asset_types asset_types_pk; Type: CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_types
    ADD CONSTRAINT asset_types_pk PRIMARY KEY (id_asset_type);


--
-- TOC entry 3073 (class 2606 OID 32892)
-- Name: assets assets_pk; Type: CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.assets
    ADD CONSTRAINT assets_pk PRIMARY KEY (id_asset);


--
-- TOC entry 3051 (class 2606 OID 16480)
-- Name: customers newtable_pk; Type: CONSTRAINT; Schema: customers; Owner: -
--

ALTER TABLE ONLY customers.customers
    ADD CONSTRAINT newtable_pk PRIMARY KEY (id_customer);


--
-- TOC entry 3053 (class 2606 OID 16482)
-- Name: customers newtable_un; Type: CONSTRAINT; Schema: customers; Owner: -
--

ALTER TABLE ONLY customers.customers
    ADD CONSTRAINT newtable_un UNIQUE (customer_internal_alias);


--
-- TOC entry 3049 (class 2606 OID 16445)
-- Name: employee_absence_codes employee_absence_code_pk; Type: CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_absence_codes
    ADD CONSTRAINT employee_absence_code_pk PRIMARY KEY (id_employee_absence_code);


--
-- TOC entry 3043 (class 2606 OID 16401)
-- Name: employees employee_pk; Type: CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employees
    ADD CONSTRAINT employee_pk PRIMARY KEY (id_employee);


--
-- TOC entry 3047 (class 2606 OID 16412)
-- Name: employee_types employee_type_pk; Type: CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_types
    ADD CONSTRAINT employee_type_pk PRIMARY KEY (id_employee_type);


--
-- TOC entry 3045 (class 2606 OID 16447)
-- Name: employees employee_un; Type: CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employees
    ADD CONSTRAINT employee_un UNIQUE (employee_internal_alias);


--
-- TOC entry 3057 (class 2606 OID 16523)
-- Name: currencies curency_pk; Type: CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.currencies
    ADD CONSTRAINT curency_pk PRIMARY KEY (id_currency);


--
-- TOC entry 3055 (class 2606 OID 24611)
-- Name: invoice_texts customer_invoice_text_pk; Type: CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.invoice_texts
    ADD CONSTRAINT customer_invoice_text_pk PRIMARY KEY (id_invoice_text);


--
-- TOC entry 3063 (class 2606 OID 24599)
-- Name: sales_invoices invoice_pk; Type: CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.sales_invoices
    ADD CONSTRAINT invoice_pk PRIMARY KEY (id_sales_invoice);


--
-- TOC entry 3061 (class 2606 OID 24587)
-- Name: invoice_states invoice_status_pk; Type: CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.invoice_states
    ADD CONSTRAINT invoice_status_pk PRIMARY KEY (id_invoice_state);


--
-- TOC entry 3069 (class 2606 OID 32818)
-- Name: payment_conditions payment_conditions_pk; Type: CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.payment_conditions
    ADD CONSTRAINT payment_conditions_pk PRIMARY KEY (id_payment_condition);


--
-- TOC entry 3071 (class 2606 OID 33028)
-- Name: service_invoices service_invoices_pk; Type: CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.service_invoices
    ADD CONSTRAINT service_invoices_pk PRIMARY KEY (id_service_invoice);


--
-- TOC entry 3065 (class 2606 OID 32781)
-- Name: products product_pk; Type: CONSTRAINT; Schema: sales; Owner: -
--

ALTER TABLE ONLY sales.products
    ADD CONSTRAINT product_pk PRIMARY KEY (id_product);


--
-- TOC entry 3059 (class 2606 OID 32945)
-- Name: sales sales_pk; Type: CONSTRAINT; Schema: sales; Owner: -
--

ALTER TABLE ONLY sales.sales
    ADD CONSTRAINT sales_pk PRIMARY KEY (id_sale);


--
-- TOC entry 3087 (class 2606 OID 33004)
-- Name: service_states service_states_pk; Type: CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.service_states
    ADD CONSTRAINT service_states_pk PRIMARY KEY (id_service_state);


--
-- TOC entry 3093 (class 2606 OID 33065)
-- Name: service_templates service_templates_pk; Type: CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.service_templates
    ADD CONSTRAINT service_templates_pk PRIMARY KEY (id_service_template);


--
-- TOC entry 3089 (class 2606 OID 33006)
-- Name: service_types service_types_pk; Type: CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.service_types
    ADD CONSTRAINT service_types_pk PRIMARY KEY (id_service_type);


--
-- TOC entry 3085 (class 2606 OID 33002)
-- Name: services services_pk; Type: CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.services
    ADD CONSTRAINT services_pk PRIMARY KEY (id_service);


--
-- TOC entry 3095 (class 2606 OID 33091)
-- Name: subcontractors subcontractors_pk; Type: CONSTRAINT; Schema: subcontractor; Owner: -
--

ALTER TABLE ONLY subcontractor.subcontractors
    ADD CONSTRAINT subcontractors_pk PRIMARY KEY (id_subcontractor);


--
-- TOC entry 3067 (class 2606 OID 32797)
-- Name: sys_rec_states sys_rec_states_pk; Type: CONSTRAINT; Schema: sys; Owner: -
--

ALTER TABLE ONLY sys.sys_rec_states
    ADD CONSTRAINT sys_rec_states_pk PRIMARY KEY (id_sys_rec_status);


--
-- TOC entry 3091 (class 2606 OID 33044)
-- Name: units units_pk; Type: CONSTRAINT; Schema: sys; Owner: -
--

ALTER TABLE ONLY sys.units
    ADD CONSTRAINT units_pk PRIMARY KEY (id_unit);


--
-- TOC entry 3114 (class 2606 OID 32934)
-- Name: asset_absences asset_absences_fk; Type: FK CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_absences
    ADD CONSTRAINT asset_absences_fk FOREIGN KEY (fk_asset_absence_code) REFERENCES assets.asset_absence_codes(id_asset_absence_code);


--
-- TOC entry 3115 (class 2606 OID 32939)
-- Name: asset_absences asset_absences_fk_1; Type: FK CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_absences
    ADD CONSTRAINT asset_absences_fk_1 FOREIGN KEY (fk_asset) REFERENCES assets.assets(id_asset);


--
-- TOC entry 3116 (class 2606 OID 33112)
-- Name: asset_allocation asset_allocation_fk; Type: FK CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_allocation
    ADD CONSTRAINT asset_allocation_fk FOREIGN KEY (fk_asset) REFERENCES assets.assets(id_asset);


--
-- TOC entry 3117 (class 2606 OID 33117)
-- Name: asset_allocation asset_allocation_fk_1; Type: FK CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_allocation
    ADD CONSTRAINT asset_allocation_fk_1 FOREIGN KEY (fk_customer) REFERENCES customers.customers(id_customer);


--
-- TOC entry 3118 (class 2606 OID 33122)
-- Name: asset_allocation asset_allocation_fk_2; Type: FK CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.asset_allocation
    ADD CONSTRAINT asset_allocation_fk_2 FOREIGN KEY (fk_employee) REFERENCES employees.employees(id_employee);


--
-- TOC entry 3112 (class 2606 OID 32904)
-- Name: assets assets_fk; Type: FK CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.assets
    ADD CONSTRAINT assets_fk FOREIGN KEY (fk_asset_type) REFERENCES assets.asset_types(id_asset_type);


--
-- TOC entry 3113 (class 2606 OID 33107)
-- Name: assets assets_rec_status; Type: FK CONSTRAINT; Schema: assets; Owner: -
--

ALTER TABLE ONLY assets.assets
    ADD CONSTRAINT assets_rec_status FOREIGN KEY (fk_sys_rec_state) REFERENCES sys.sys_rec_states(id_sys_rec_status);


--
-- TOC entry 3100 (class 2606 OID 32798)
-- Name: customers customers_fk; Type: FK CONSTRAINT; Schema: customers; Owner: -
--

ALTER TABLE ONLY customers.customers
    ADD CONSTRAINT customers_fk FOREIGN KEY (fk_sys_rec_status) REFERENCES sys.sys_rec_states(id_sys_rec_status);


--
-- TOC entry 3098 (class 2606 OID 16454)
-- Name: employee_absences employee_absence_fk; Type: FK CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_absences
    ADD CONSTRAINT employee_absence_fk FOREIGN KEY (fk_employee_absence_code) REFERENCES employees.employee_absence_codes(id_employee_absence_code);


--
-- TOC entry 3099 (class 2606 OID 16459)
-- Name: employee_absences employee_absence_fk_1; Type: FK CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employee_absences
    ADD CONSTRAINT employee_absence_fk_1 FOREIGN KEY (fk_employee) REFERENCES employees.employees(id_employee);


--
-- TOC entry 3097 (class 2606 OID 32803)
-- Name: employees employees_fk; Type: FK CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employees
    ADD CONSTRAINT employees_fk FOREIGN KEY (fk_sys_rec_status) REFERENCES sys.sys_rec_states(id_sys_rec_status);


--
-- TOC entry 3096 (class 2606 OID 16414)
-- Name: employees fk_employee_type; Type: FK CONSTRAINT; Schema: employees; Owner: -
--

ALTER TABLE ONLY employees.employees
    ADD CONSTRAINT fk_employee_type FOREIGN KEY (fk_employee_type) REFERENCES employees.employee_types(id_employee_type);


--
-- TOC entry 3101 (class 2606 OID 16508)
-- Name: invoice_texts customer_invoice_text_fk; Type: FK CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.invoice_texts
    ADD CONSTRAINT customer_invoice_text_fk FOREIGN KEY (fk_customer) REFERENCES customers.customers(id_customer);


--
-- TOC entry 3108 (class 2606 OID 33132)
-- Name: payment_conditions payment_conditions_fk; Type: FK CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.payment_conditions
    ADD CONSTRAINT payment_conditions_fk FOREIGN KEY (fk_currency) REFERENCES finance.currencies(id_currency);


--
-- TOC entry 3104 (class 2606 OID 32864)
-- Name: sales_invoices sales_invoices_fk; Type: FK CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.sales_invoices
    ADD CONSTRAINT sales_invoices_fk FOREIGN KEY (fk_payment_conditions) REFERENCES finance.payment_conditions(id_payment_condition);


--
-- TOC entry 3105 (class 2606 OID 32869)
-- Name: sales_invoices sales_invoices_fk_1; Type: FK CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.sales_invoices
    ADD CONSTRAINT sales_invoices_fk_1 FOREIGN KEY (fk_invoice_text) REFERENCES finance.invoice_texts(id_invoice_text);


--
-- TOC entry 3106 (class 2606 OID 32874)
-- Name: sales_invoices sales_invoices_fk_2; Type: FK CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.sales_invoices
    ADD CONSTRAINT sales_invoices_fk_2 FOREIGN KEY (fk_invoice_state) REFERENCES finance.invoice_states(id_invoice_state);


--
-- TOC entry 3109 (class 2606 OID 32849)
-- Name: service_invoices service_invoices_fk; Type: FK CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.service_invoices
    ADD CONSTRAINT service_invoices_fk FOREIGN KEY (fk_payment_condition) REFERENCES finance.payment_conditions(id_payment_condition);


--
-- TOC entry 3110 (class 2606 OID 32854)
-- Name: service_invoices service_invoices_fk_1; Type: FK CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.service_invoices
    ADD CONSTRAINT service_invoices_fk_1 FOREIGN KEY (fk_invoice_text) REFERENCES finance.invoice_texts(id_invoice_text);


--
-- TOC entry 3111 (class 2606 OID 32859)
-- Name: service_invoices service_invoices_fk_2; Type: FK CONSTRAINT; Schema: finance; Owner: -
--

ALTER TABLE ONLY finance.service_invoices
    ADD CONSTRAINT service_invoices_fk_2 FOREIGN KEY (fk_invoice_state) REFERENCES finance.invoice_states(id_invoice_state);


--
-- TOC entry 3107 (class 2606 OID 33050)
-- Name: products products_fk; Type: FK CONSTRAINT; Schema: sales; Owner: -
--

ALTER TABLE ONLY sales.products
    ADD CONSTRAINT products_fk FOREIGN KEY (fk_unit) REFERENCES sys.units(id_unit);


--
-- TOC entry 3102 (class 2606 OID 32782)
-- Name: sales sales_fk; Type: FK CONSTRAINT; Schema: sales; Owner: -
--

ALTER TABLE ONLY sales.sales
    ADD CONSTRAINT sales_fk FOREIGN KEY (fk_product) REFERENCES sales.products(id_product);


--
-- TOC entry 3103 (class 2606 OID 33127)
-- Name: sales sales_sales_invoice; Type: FK CONSTRAINT; Schema: sales; Owner: -
--

ALTER TABLE ONLY sales.sales
    ADD CONSTRAINT sales_sales_invoice FOREIGN KEY (fk_invoice) REFERENCES finance.sales_invoices(id_sales_invoice);


--
-- TOC entry 3119 (class 2606 OID 33007)
-- Name: services service_state; Type: FK CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.services
    ADD CONSTRAINT service_state FOREIGN KEY (fk_service_state) REFERENCES services.service_states(id_service_state);


--
-- TOC entry 3128 (class 2606 OID 33137)
-- Name: service_templates service_templates_customer; Type: FK CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.service_templates
    ADD CONSTRAINT service_templates_customer FOREIGN KEY (fk_customer) REFERENCES customers.customers(id_customer);


--
-- TOC entry 3126 (class 2606 OID 33066)
-- Name: service_templates service_templates_fk; Type: FK CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.service_templates
    ADD CONSTRAINT service_templates_fk FOREIGN KEY (fk_service_type) REFERENCES services.service_types(id_service_type);


--
-- TOC entry 3127 (class 2606 OID 33071)
-- Name: service_templates service_templates_fk_1; Type: FK CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.service_templates
    ADD CONSTRAINT service_templates_fk_1 FOREIGN KEY (fk_unit) REFERENCES sys.units(id_unit);


--
-- TOC entry 3122 (class 2606 OID 33022)
-- Name: services services_asset_allocation; Type: FK CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.services
    ADD CONSTRAINT services_asset_allocation FOREIGN KEY (fk_asset_allocation) REFERENCES assets.asset_allocation(id_asset_allocation);


--
-- TOC entry 3121 (class 2606 OID 33017)
-- Name: services services_customer; Type: FK CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.services
    ADD CONSTRAINT services_customer FOREIGN KEY (fk_customer) REFERENCES customers.customers(id_customer);


--
-- TOC entry 3123 (class 2606 OID 33045)
-- Name: services services_fk; Type: FK CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.services
    ADD CONSTRAINT services_fk FOREIGN KEY (fk_unit) REFERENCES sys.units(id_unit);


--
-- TOC entry 3125 (class 2606 OID 33102)
-- Name: services services_service_invoice; Type: FK CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.services
    ADD CONSTRAINT services_service_invoice FOREIGN KEY (fk_invoice) REFERENCES finance.service_invoices(id_service_invoice);


--
-- TOC entry 3124 (class 2606 OID 33097)
-- Name: services services_subcontractors; Type: FK CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.services
    ADD CONSTRAINT services_subcontractors FOREIGN KEY (fk_subcontractor) REFERENCES subcontractor.subcontractors(id_subcontractor);


--
-- TOC entry 3120 (class 2606 OID 33012)
-- Name: services services_type; Type: FK CONSTRAINT; Schema: services; Owner: -
--

ALTER TABLE ONLY services.services
    ADD CONSTRAINT services_type FOREIGN KEY (fk_service_type) REFERENCES services.service_types(id_service_type);


--
-- TOC entry 3129 (class 2606 OID 33092)
-- Name: subcontractors subcontractors_fk; Type: FK CONSTRAINT; Schema: subcontractor; Owner: -
--

ALTER TABLE ONLY subcontractor.subcontractors
    ADD CONSTRAINT subcontractors_fk FOREIGN KEY (fk_sys_rec_status) REFERENCES sys.sys_rec_states(id_sys_rec_status);


-- Completed on 2023-07-31 21:22:53 CEST

--
-- PostgreSQL database dump complete
--

