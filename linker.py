from fuzzywuzzy import fuzz



from recordlinkage.base import BaseIndexAlgorithm

class EasySimilarityIndex(BaseIndexAlgorithm):
    
    """Custom class for indexing"""
    
    def __init__(self, index_a, index_b, threshold=0.4):
        
        super(EasySimilarityIndex, self).__init__()
        
        self.index_a = index_a
        self.index_b = index_b
        self.threshold = threshold
        
        print("Indexer was initialized!")
    
    

    def _link_index(self, df_a, df_b):
        
        
        """Make pairs with given names starting with the letter 'w'."""
        
        
        # Create sorted name column
        dfaSeries = df_a[self.index_a].apply(self._sort_Alphabetically)
        dfbSeries = df_b[self.index_b].apply(self._sort_Alphabetically)
        
        output_pairs = []
        
        
        for cur_index_a, string_a in dfaSeries.iteritems():
            
            
            for cur_index_b, string_b in dfbSeries.iteritems():
                
                # Comparing string_a with string_b
                similarity_result = fuzz.ratio(string_a, string_b)
                
                if similarity_result > self.threshold*100:
                    
                    
                    output_pairs.append((cur_index_a, cur_index_b))
        

        # Make a product of the two numpy arrays
        return pandas.MultiIndex.from_tuples(
            output_pairs,
            names=(self.index_a, self.index_a)
            
        )
    
    
    def _sort_Alphabetically(self, string):
        
        """Sorting a string alphabetically"""
        
        return "".join(sorted(string))
    
class PartialSimilarityIndex(BaseIndexAlgorithm):
    
    """Custom class for indexing"""
    
    def __init__(self, index_a, index_b, threshold=0.4):
        
        super(PartialSimilarityIndex, self).__init__()
        
        self.index_a = index_a
        self.index_b = index_b
        self.threshold = threshold
        
        print("Indexer was initialized!")
    
    

    def _link_index(self, df_a, df_b):
        
        
        """Make pairs with given names starting with the letter 'w'."""
        
        
        # Create sorted name column
        dfaSeries = df_a[self.index_a].copy()
        dfbSeries = df_b[self.index_b].copy()
        
        output_pairs = []
        
        
        for cur_index_a, string_a in dfaSeries.iteritems():
            
            
            for cur_index_b, string_b in dfbSeries.iteritems():
                
                # Comparing string_a with string_b
                similarity_result = fuzz.token_sort_ratio(string_a, string_b)
                
                if similarity_result > self.threshold*100:
                    
                    
                    output_pairs.append((cur_index_a, cur_index_b))
        

        # Make a product of the two numpy arrays
        return pandas.MultiIndex.from_tuples(
            output_pairs,
            names=(self.index_a, self.index_a)
            
        )
    
    
    def _sort_Alphabetically(self, string):
        
        """Sorting a string alphabetically"""
        
        return "".join(sorted(string))

