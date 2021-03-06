# Create a DataSet object for each of the programs we track.  
# Initialize each one with the information it needs to do its query
# of the database.
# Store the DataSet objects in a dictionary with keys being the
# friendly names of the program, which will be used in selection
# widgets.

# In the following line, 'from DataSet' refers to the file DataSet.py
# while 'import DataSet' refers to the DataSet class within DataSet.py.

from ECHO_modules.DataSet import DataSet

def make_data_sets():
    data_sets = {}
    
    ds = DataSet( name='RCRA Violations', idx_field='ID_NUMBER', 
                    table_name='RCRA_VIOLATIONS', echo_type="RCRA",
                    date_field='DATE_VIOLATION_DETERMINED', date_format='%m/%d/%Y', agg_type = "count", agg_col="VIOL_DETERMINED_BY_AGENCY", unit="violations") # For possible later use in assessing state v federal 
    data_sets[ ds.name ] = ds
    ds = DataSet( name='RCRA Inspections', idx_field='ID_NUMBER', 
                    table_name='RCRA_EVALUATIONS', echo_type="RCRA",
                    date_field='EVALUATION_START_DATE', date_format='%m/%d/%Y', agg_type = "count", agg_col="EVALUATION_AGENCY", unit="inspections") # For possible later use in assessing state v federal 
    data_sets[ ds.name ] = ds
    ds = DataSet( name='RCRA Penalties',  echo_type="RCRA",
                    table_name='RCRA_ENFORCEMENTS', idx_field='ID_NUMBER', 
                    date_field='ENFORCEMENT_ACTION_DATE', date_format='%m/%d/%Y', agg_type = "sum", agg_col="Penalties", unit="dollars")
    data_sets[ ds.name ] = ds
    ds = DataSet( name='CAA Violations',  echo_type="AIR",
                    table_name='ICIS-AIR_VIOLATION_HISTORY', idx_field='pgm_sys_id', 
                    date_field='HPV_DAYZERO_DATE', date_format='%m-%d-%Y', agg_type = "count", agg_col="AGENCY_TYPE_DESC", unit="violations") # For possible later use in assessing state v federal 
    data_sets[ ds.name ] = ds
    ds = DataSet( name='CAA Inspections', echo_type="AIR",
                    table_name='ICIS-AIR_FCES_PCES', idx_field='PGM_SYS_ID',
                    date_field='ACTUAL_END_DATE', date_format='%m-%d-%Y' , agg_type = "count", agg_col="STATE_EPA_FLAG", unit="inspections") # For possible later use in assessing state v federal 
    data_sets[ ds.name ] = ds
    ds = DataSet( name='CAA Penalties', echo_type="AIR",
                    table_name='ICIS-AIR_FORMAL_ACTIONS', idx_field='pgm_sys_id',
                    date_field='SETTLEMENT_ENTERED_DATE', date_format='%m/%d/%Y' , agg_type = "sum", agg_col="PENALTY_AMOUNT", unit="dollars")
    data_sets[ ds.name ] = ds
    my_sql = "select * from `POLL_RPT_COMBINED_EMISSIONS` " + \
                " where PGM_SYS_ACRNM = 'E-GGRT' and REGISTRY_ID in "
    ds = DataSet( name='Greenhouse Gas Emissions', echo_type="GHG",
                    table_name='POLL_RPT_COMBINED_EMISSIONS', idx_field='REGISTRY_ID',
                    date_field='REPORTING_YEAR', date_format='%Y', sql = my_sql, agg_type = "sum", agg_col="ANNUAL_EMISSION", unit="metric tons of CO2 equivalent")
    data_sets[ ds.name ] = ds
    ds = DataSet( name='CWA Violations', echo_type="NPDES",
                    table_name='NPDES_QNCR_HISTORY', idx_field='NPDES_ID',
                    date_field='YEARQTR', date_format='%Y' , agg_type = "sum", agg_col="NUME90Q", unit="effluent violations")
    data_sets[ ds.name ] = ds
    ds = DataSet( name='CWA Inspections', echo_type="NPDES",
                    table_name='NPDES_INSPECTIONS', idx_field='NPDES_ID',
                    date_field='ACTUAL_END_DATE', date_format='%m/%d/%Y', agg_type = "count", agg_col="STATE_EPA_FLAG", unit="inspections") # For possible later use in assessing state v federal 
    data_sets[ ds.name ] = ds
    ds = DataSet( name='CWA Penalties', echo_type="NPDES",
                    table_name='NPDES_FORMAL_ENFORCEMENT_ACTIONS', idx_field='NPDES_ID',
                    date_field='SETTLEMENT_ENTERED_DATE', date_format='%m/%d/%Y', agg_type = "sum", agg_col="Penalties", unit="dollars")
    data_sets[ ds.name ] = ds

    return data_sets