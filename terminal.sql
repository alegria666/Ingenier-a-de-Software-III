--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: abordajes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.abordajes (
    id_cedula smallint,
    idruta smallint
);


ALTER TABLE public.abordajes OWNER TO postgres;

--
-- Name: bus; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bus (
    idbus smallint NOT NULL,
    placa character(7),
    capacidad smallint,
    idempleado smallint
);


ALTER TABLE public.bus OWNER TO postgres;

--
-- Name: cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente (
    id_cedula smallint NOT NULL,
    nombre character varying,
    apellido character varying,
    telefono character(12),
    correo character varying
);


ALTER TABLE public.cliente OWNER TO postgres;

--
-- Name: empleado; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.empleado (
    idempleado smallint NOT NULL,
    nombre character varying,
    apellido character varying,
    telefono character(12),
    cedula character(10)
);


ALTER TABLE public.empleado OWNER TO postgres;

--
-- Name: rutas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rutas (
    idruta smallint NOT NULL,
    salida character varying,
    destino character varying,
    horario timestamp without time zone,
    idbus smallint
);


ALTER TABLE public.rutas OWNER TO postgres;

--
-- Data for Name: abordajes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.abordajes (id_cedula, idruta) FROM stdin;
1001	4001
1002	4001
1003	4001
1004	4002
1005	4002
1003	4002
\.


--
-- Data for Name: bus; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bus (idbus, placa, capacidad, idempleado) FROM stdin;
3001	KMZ-323	35	2002
3002	UJL-123	40	2003
3003	KRF-543	15	2001
3004	UYO-234	25	2002
\.


--
-- Data for Name: cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cliente (id_cedula, nombre, apellido, telefono, correo) FROM stdin;
1001	Fabio	Buldweiser	3122521312  	fabio@xmail.com
1002	Antonella	Luna	3151251312  	antonella@xmail.com
1003	Deisy	Timaran	3215641254  	deisy@xmail.com
1004	Juan	Di Stefano	3235267875  	juan@xmail.com
1005	Pepe	Sanchez	3002564123  	pepe@xmail.com
1006	Daniel	Alegria	54353       	daniel@xmail.com
1007	Santiago	Rayao	321543      	santiago@xmail.com
\.


--
-- Data for Name: empleado; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.empleado (idempleado, nombre, apellido, telefono, cedula) FROM stdin;
2001	Arturo	Vidal	3125261214  	1108251436
2002	Ruth	Halland	3256523214  	1125635225
2003	Killyan	Hernandez	3184562145  	1002523652
2004	Atreus	Goretzka	3122652222  	1365225655
2005	Carlos	Cuahutemoc	3195623654  	1000252156
2006	German	Erazo	3122600585  	32252     
\.


--
-- Data for Name: rutas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.rutas (idruta, salida, destino, horario, idbus) FROM stdin;
4001	Ipiales	Pasto	2023-07-15 20:00:00	3002
4002	Pasto	Cali	2023-07-16 15:00:00	3004
4003	Ipiales	Cali	2023-08-15 21:00:00	3003
\.


--
-- Name: bus bus_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus
    ADD CONSTRAINT bus_pkey PRIMARY KEY (idbus);


--
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (id_cedula);


--
-- Name: empleado empleado_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.empleado
    ADD CONSTRAINT empleado_pkey PRIMARY KEY (idempleado);


--
-- Name: rutas rutas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rutas
    ADD CONSTRAINT rutas_pkey PRIMARY KEY (idruta);


--
-- Name: abordajes abordajes_id_cedula_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.abordajes
    ADD CONSTRAINT abordajes_id_cedula_fkey FOREIGN KEY (id_cedula) REFERENCES public.cliente(id_cedula);


--
-- Name: abordajes abordajes_idruta_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.abordajes
    ADD CONSTRAINT abordajes_idruta_fkey FOREIGN KEY (idruta) REFERENCES public.rutas(idruta);


--
-- Name: bus bus_idempleado_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus
    ADD CONSTRAINT bus_idempleado_fkey FOREIGN KEY (idempleado) REFERENCES public.empleado(idempleado);


--
-- Name: rutas rutas_idbus_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rutas
    ADD CONSTRAINT rutas_idbus_fkey FOREIGN KEY (idbus) REFERENCES public.bus(idbus);


--
-- PostgreSQL database dump complete
--

