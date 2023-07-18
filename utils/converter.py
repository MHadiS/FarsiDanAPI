class ListConverter:
    regex = "[ -~]+,"
    
    def to_python(self, value:str):
        items = value[:len(value) - 1].split(",")
        formatted_items = []

        for item in items:
            item = item.strip()
            formatted_items.append(item)

        return formatted_items
    
    def to_url(self, value):
        return ",".join(value)