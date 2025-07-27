from bs4 import BeautifulSoup


def single_page(content) :
    
    keys = []
    page_list = []
    try :


        soup = BeautifulSoup(content, "html.parser")

        thead = soup.select_one("table.table.table-striped.uk-margin thead")
        thead = thead.select("th")

        for title in thead[:4] :
            keys.append(title.text.strip())


        tbody = soup.select_one("table.table.table-striped.uk-margin tbody")
        tbody = tbody.select("tr")


        for tr in tbody :
            values = []
            for td in tr.select("td") :
                values.append(td.text.strip())
            mydict = {keys[i]:values[i] for i in range(len(keys))}
            page_list.append(mydict)


        return page_list    

    except : 
        return


