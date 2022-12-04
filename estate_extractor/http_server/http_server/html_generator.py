from yattag import Doc
import sqlclient as sc


sqlcli = sc.SQLClient()

def render_list(doc, tag, text, data):
    for i, item in enumerate(data):
        with tag('tr'):
            with tag('td'):
                text(i+1)
            with tag('td'):
                doc.stag('img', src=item[1], style="width:100px;")
            with tag('td'):
                text(item[0])

def render_page():
    sqlcli.refresh_data()
    data = sqlcli.get_data()
    doc, tag, text = Doc().tagtext()
    doc.asis('<!DOCTYPE html><meta charset="UTF-8">')
    with tag('html'):
        with tag('head'):
            pass
        with tag('body'):
            with tag('h3', id = 'title'):
                text('Extreacted real estate advertisements:')
                doc.stag('br')
            with tag('h5'):
                print(len(data))
                
                if len(data) == 500:
                    text('Scraping DONE. Number of real estates extracted: ' + str(len(data)))
                else:
                    text('Scraping in progress... Number of real estates already extracted: ' + str(len(data)))
                doc.stag('br')
                doc.stag('br')
            with tag('table'):
                with tag('tr', style="text-align:center;"):
                    with tag('td'):
                        with tag('b'):
                            text('Index')
                    with tag('td'):
                        with tag('b'):
                            text('Image')
                    with tag('td'):
                        with tag('b'):
                            text('Title')
                render_list(doc, tag, text, data)
    
    result = doc.getvalue()
    return result

                    

