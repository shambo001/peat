#!/usr/bin/env python
#
# Protein Engineering Analysis Tool DataBase (PEATDB)
# Copyright (C) 2010 Damien Farrell & Jens Erik Nielsen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Email: Jens.Nielsen_at_gmail.com 
# Normal mail:
# Jens Nielsen
# SBBS, Conway Institute
# University College Dublin
# Dublin 4, Ireland
# 

def logo():
     import Tkinter as tk
     logo = tk.PhotoImage(format='gif',data=
             'R0lGODlhvQC+AIcAAAAAAAYGCAgGBggHCA4IBg0NDQ0NEQ8QEhIEAhMIBhAO'
            +'DhsEARoIBRkLCBAOFRAQEBQTGhYYGxgWFhgVHxsaGgMBIQMBMxsbIRgWPR0h'
            +'JioIAysTDSAeHi0bFDMIAjIUDTQcFCAdKiQiIiIjKyUpLSgmJiwqKignNSwy'
            +'OTAuLjArPzQxMTE2OzM4PTk2Njw6OgMBQAIBVgIBYQIBdzItQjY5Rj03USso'
            +'czlDTT5KWDdFYk0KAkoUC0sdE1sMAlcVClsdEU8hFlsjFkE9PV8+L2MNAWgY'
            +'C2ceEXoPAXoXCHsfEGsiE3soF0I7V35OOn5TPkVBQUBGTEJJT0lFRU1JSUJL'
            +'VEhTXVFNTVVRUVBZX1lVVV1YWEdNY0pVZU5UcE1adE9beFFOalRaalBWc1NY'
            +'dFNceVtdc1ZiblJiclZjfFpmcV5heVxoc1tre2FdXWplZWFpeGVyfXJtbXp0'
            +'dAEBqAEB0gEB6TZVjkJfmERhmkhlnlZpgVlkgVttglpui15whV9ykkpnoE1q'
            +'o1BspVJvqFVxqlh1rlp3sF15smd4iWd6lXR7iXJ+k2x+omF9tmN/uEhGyFBN'
            +'3m2BlHSBjXeGl2+JpmWBummFvnaIpnuKtXuSq3qWtFyJ3kuJ+16L4GuHwG2J'
            +'wnGMxXyUymGO42eT6YYbCpQWBYUlE5MoFZYyHogzIKkUALsXAaEjD6MpE70l'
            +'Dr4qEqw7JKxBKYJ9fcYaA9YaAcYkDMgrEsczGdgnDdI4HOIcAvAcAOIlCeUu'
            +'EuI6HfAjB/EuEPEzFeQ/IcxFKcZMMNFFKeBAIoqEhICKnIGRnpKMjJqTk4OM'
            +'o4GOsYmZq4eXtZCfqZSat4+grYqhuJChrZOouZ6xvaObm6ujo7OsrLqysomY'
            +'x4Kd1pKdxJCd0Yelxouu1JarxZSl1ZqzyZi315Sv4Zm15KOqzKSs06K5y6S6'
            +'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'
            +'Hl5ylv9T4QoRd/QCAgA7')
     return logo
     
def next():
     import Tkinter as tk
     next = tk.PhotoImage(format='gif',data=      
             'R0lGODlhEAAQAIcAAAAAACBeHSRjISlpJS9wKjV4LzuANUKIO0WIP0mLREqM'
            +'RUmRQU+ZR1CRSlydVVahTV6hWVypU2KjWmKxWGi4XW2+YXy+dnHDZXTHaIDB'
            +'eoLCfYTDfofFgYnGgovHhY7Jh5DKiZPLi5XMjpjOkJrPk53QlJ/SlqHTmKPU'
            +'mqXVnKfWnqnXoKvYoq7apQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAACH5BAEAAC4ALAAAAAAQABAAAAheAF0IHEiwoMGD'
            +'CBMqXJiQAcOBCw4QxIDhQgUKEyI8YLBAgoMCAzG0YKEChQkSIkB44KChwQCB'
            +'F1akOFFiRIgPHTZksKBAgMCLGTdGNIAAQgKfDAcgZbj0odOnUA8GBAA7')
     return next
    
def prev():
     import Tkinter as tk    
     prev = tk.PhotoImage(format='gif',data=    
             'R0lGODlhEAAQAIcAAAAAACBeHSRjISlpJS9wKjV4LzuANUKIO0mRQU+ZR1ah'
            +'TVypU2SqW2KxWGi4XXi9cnu+cXy+dnHDZXTHaH7AeIDBeoPBeoLCfYTDfobI'
            +'e4fJfIrMf4fFgYnGgovHhYvNgI7Jh5DKiZPLi5XMjpjOkJrPk53QlJ/SlqHT'
            +'mKPUmqXVnKfWnqvYogAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAACH5BAMAAC0ALAAAAAAQABAAAAhdAFsIHEiwoMGD'
            +'CBMqXChwAsOGEh5O+KDBQYMFChIgOGCgAIGGG1isSHGixIgQHjhcoDBAoIQM'
            +'KlCYICECRAcMFSI8EDDQAQQLDDRy9DhAQACCGB8KTKC0qdOnDwMCADs=')
     return prev

def add():
     import Tkinter as tk    
     add = tk.PhotoImage(format='gif',data=
             'R0lGODlhEAAQAIcAAAAAADB/KDB/KTOBLDSBLDSCLDeELzmFMDyHMj2INECJ'
            +'NkKNNkKLOEOPOESMOkeOPEmPPUyRQE6SQVGURFOWRVCZQVeeRVaYSFiZSVub'
            +'TF2cTV+eUGGfUWWhVGajVmWrVWmlWGumWWirU2uqWGqsW2yqWm6oXG61WG+1'
            +'WG+1WXCpXXS3W3S3XHC4WXK5W3O6XHG+X3OrYHWsYXeuY3qvZXe8YHi0ZHyx'
            +'Z36yaXy6ZH28Zn2+Z3m9bn25an25a3+5bXDBY3nBZHrGa3zDa37BaX7Hb4Cz'
            +'aoO1bYS2boe4cIe4cYi5cYq6c4u7c4u7dIm+eI2+e4HMdYbJeobJfIXNeYrC'
            +'eY/CfYnIf4rPfYzLgY7MhI7Sg5LFgJfHhZfMhZPNiJjLhpjMh5jMipTTipbT'
            +'iZXUipbUi5fVi5nRi53YkqTOlKbPlqbQlqDZlaDZlqXbm6rUnavUnK/fpa/f'
            +'prPZpbTZpbTaprLbqLPdqbXbqLfaqrTdqrXfrLbdrLjdr7vcr7fgr77itr3k'
            +'tsXowMvmw87pydTrz9fu0tzx2ODy3P///wAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAACH5BAMAAIsALAAAAAAQABAAAAi6ABcJHEiwoMFF'
            +'SIzcmBHjoEAlaggZKuTnB4iDSf4kEvTGjZxBVTYUTKIHUZovWsyU2QLIxwWC'
            +'XQ61GXNFkSIqQ4rwsRBB4JE+c7JM4WGTRI0XaLg8EIgj0BkpNqMqakEEDgOB'
            +'NPBgiSLVZosdcRIIlCGGjBAgH7y2cOEFygGBKkTsCQKjhtcTLOw0IOihx52j'
            +'LVKgWEGnRIGCGmzkCaMjB5g6IwgcpFDBCps1TxZIdgjBgQIEBhyKLhgQADs=')   
        
     return add
     
def delb():
     import Tkinter as tk    
     delb = tk.PhotoImage(format='gif',data=
             'R0lGODlhEAAQAIcAAAAAALVIJ7VLKbdKK7dMK7hKKrpLLrhOLrxLML5PNrxQ'
            +'Mr1RNb5TOMFNM8RQNMBTOsJQOsJUPsNUP8xSPNBPPsVWQcZVQsdXRchYRspY'
            +'SMtZScxbTM1aTc5dUNtWS9FeU9JfVNddUc9hU9ZgVNRgWNRiWNZjW9diXNlj'
            +'XdpjX9pkYdxkY9tpZN5qZ91qaN9qauZWTOZYTOZZTulZTelbT+ZWUOZaUudd'
            +'WepcUOxfVOBlXO5mUuljW+pmXO5qXvBkVvNzXeNrYeNuY+BpauFqa+FsbOJt'
            +'beNsbeJwZuJ7deR4cel7cOh6del/ePJ3Y/N5Y+qDfe6Efe+Gfu6KdfaCaPaE'
            +'bPCFcPCDe/CMd/GOeviGcPiMdvCRf/eRfveTfvmSfvqTf/iUf+6Mge2Tju6S'
            +'j/SOgfqah/qdi/GclvGdlvSgnvSinvWjn/qjkfupnPqrnfOno/Wmoferofar'
            +'ovWsofWvpfKtqvivpPS0qvi2qPm5r/q6rvjDvvzHuvnLxPnTzPzUzf3b1P3c'
            +'2P///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAACH5BAMAAIQALAAAAAAQABAAAAi2AAkJHEiwoEFC'
            +'LlaoQGHioMAXY/j88YMHyYeDQ+wI2tPmjJs+SzYUHAInkBkuWcJ82ZJHyAWC'
            +'UACd8TKlis0qT+5QiCCwRZ03WHIIHeqkTJMHAlnoAWNlkNOnM3ykSSAwhRwt'
            +'VJ5C7YFGgcATYroAmUG2LI0rSQwIJOFhzo8dZWfEsMHGAUERQejkwDFDBowa'
            +'a0YUKKhBRxwpPG5EURNiwEELE5iQIaOkgWOHEBgsQHDAoeeCAQEAOw==')
                
     return delb

