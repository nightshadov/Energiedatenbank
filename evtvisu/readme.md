django framework for visualisation and string data from parser into db

# Examples

## Adding new data

### Experiment Log

To add new data, issue a POST request to ``api/newExperimentLog``. If you don't set all required fields, the POST
request will be successful, but it won't be saved to the database. An error log will appear in the Django console.

A fully valid POST request would contain the following json:

```json
{
  "time": "2021-01-01T11:23:42",
  "t1_br_actual": 100.0,
  "t3_br_actual": 0.0,
  "t4_br_actual": 0.0,
  "t1_bk_actual": 0.0,
  "t1_bk_target": 0.0,
  "t2_bk_actual": 0.0,
  "t2_bk_target": 0.0,
  "t3_bk_actual": 0.0,
  "t3_bk_target": 0.0,
  "t4_bk_actual": 0.0,
  "t4_bk_target": 0.0,
  "t5_bk_actual": 0.0,
  "t5_bk_target": 0.0,
  "t6_bk_actual": 0.0,
  "t2_rz_actual": 0.0,
  "t2_rz_target": 0.0,
  "t3_rz_actual": 0.0,
  "t3_rz_target": 0.0,
  "t1_rg_actual": 0.0,
  "t1_rg_target": 0.0,
  "t2_rg_actual": 0.0,
  "t1_ms_actual": 0.0,
  "t2_ms_actual": 0.0,
  "t3_ms_actual": 0.0,
  "t4_ms_actual": 0.0,
  "p1_br_actual": 0.0,
  "p1_br_target": 0.0,
  "p1_r_actual ": 0.0,
  "p1_rg_actual": 0.0,
  "p1_rlkl_actual": 0.0,
  "p1_rz_actual": 0.0,
  "p2_rz_actual": 0.0,
  "dp1_rg_actual ": 0.0,
  "dp1_rz_actual ": 0.0,
  "dp2_rz_actual ": 0.0,
  "coal_m_actual ": 0.0,
  "m1_rz_actual": 0.0,
  "m1_rz_target": 0.0,
  "m2_rz_actual": 0.0,
  "m2_rz_target": 0.0,
  "m1_rl_actual": 0.0,
  "m1_rl_target": 0.0,
  "m2_rl_actual": 0.0,
  "m2_rl_target": 0.0,
  "mfc1_o2_actual": 0.0,
  "mfc1_o2_target": 0.0,
  "mfc2_o2_actual": 0.0,
  "mfc2_o2_target": 0.0,
  "coal_density": 0.0,
  "venturi_density": 0.0
}

```

### ALMEMO Log

To add new data, issue a POST request to ``api/newAlmemoLog``. If you don't set all required fields, the POST request
will be successful, but it won't be saved to the database. An error log will appear in the Django console.

Plead note: The property "MCS H²O %" (in our data structure mcs_h2o) **is given in percent and not in a decimal number**
. Django expects a normal float, so is has to be converted (e.g. 17% -> 0.17).

A fully valid POST request would contain the following json:

```json
{
  "time": "2021-01-01T11:23:42",
  "mcs_no ": 0.0,
  "mcs_co ": 0.0,
  "mcs_co2": 0.0,
  "mcs_n2o": 0.0,
  "mcs_nh3": 0.0,
  "mcs_hcl": 0.0,
  "mcs_so2_med": 0.0,
  "mcs_so2_hi ": 0.0,
  "mcs_h2o ": 0.0,
  "mcs_o2 ": 0.0,
  "t_bk ": 0.0,
  "coal_cond": 0.0,
  "d_p_bg": 0.0,
  "coal_density": 0.0,
  "venturi_density": 0.0
}

```
