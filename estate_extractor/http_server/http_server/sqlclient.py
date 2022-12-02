
class SQLClient:
    
    items : list[list[str, str]]
    next_item_idx = 0

    def refresh_data(self) -> None:
        #TODO SQL qeury data
        self.next_item_idx = 0
        pass

    def get_data(self) -> list[list[str, str]]:
        return self.items

