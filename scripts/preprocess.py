from unittest import result


class Preprocess:

    def __init__(self) -> None:
        """Initilize class."""
        pass
    
    def get_units(self, results):
        '''
        This function returns the units found in a given results
        
        Params:
            results: Pandas.DataFrame
                    A dataframe containing the results
        
        Returns:
            A list containing the unit codes
        '''
        
        cols = results.columns.to_list()
        return cols[1:-2]
    
    def check_duplicates(self, results):
        '''
        This function checks for duplicates in a given results
        
        Params:
            results:Pandas.DataFrame
                    A dataframe containing the results
        
        Returns:
            A true there are duplicates and the total number of duplicated rows otherwise it return false and number of duplicates as 0
        '''
        
        count =results.duplicated().sum()
        if count==0:
            return False, count
        else:
            return True, count
        
    def check_nulls(self, results):
        '''
        This function checks for null values in the result
        
        Params:
            results:Pandas.DataFrame
                    A dataframe containing the results
        
        Returns:
             A true there are nulls and the total number of nulls rows otherwise it return false and number of nulls as 0
        '''
        count =results.isna().sum()
        if count==0:
            return False, count
        else:
            return True, count
        
    def get_info(self, results):
        '''
        This function retuns the information about the results dataframe
        Params:
            results:Pandas.DataFrame
                    A dataframe containing the results
        
        Returns:
             A true there are nulls and the total number of nulls rows otherwise it return false and number of nulls as 0
        '''
        
        return results.info()
    
    def unit_performance_viz(self, results, unit):
        '''
        Visualize the grade distribution in a given unit
        
        Params:
            results: Pandas.DataFrame
                    A dataframe containing the results
            unit: String
                The unit being visualized                    
        '''
        from plot import Plot
        plot = Plot()
        plot.plot_count(results, unit)
        
    def class_performance_viz(self, results):
        '''
        Visualize the class performannce
        
        Params:
            results: Pandas.DataFrame
                    A dataframe containing the results                 
        '''
        from plot import Plot
        plot = Plot()
        plot.plot_hist(results,  'REMARKS', 'red')
        
    def std_performance_viz(self, results, reg_no):
        '''
        Visualize a student's performannce
        
        Params:
            results: Pandas.DataFrame
                A dataframe containing the results 
            reg_no: String
                The Registration Number of the student whose performance is to be visualized                
        '''
        from plot import Plot
        import pandas as pd
        
        plot = Plot()        
        std = results[ (results['REG NO'] == reg_no )]      # Single record for the specified student
        units = self.get_units(results)                      # the units in the results
        rslt = pd.DataFrame(std, columns = units)
        row = rslt.iloc[0]
        row.value_counts().plot(kind='bar', ylabel='Count of Grades', xlabel='Grade')
        
        
    
    
        
        
    
        
        
        
   

 