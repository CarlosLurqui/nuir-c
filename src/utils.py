#!/usr/bin/python

import os  ;  import sys

from requests  import *
from colorama  import init as cs
from colorama  import Fore as c
from json      import *
from pystyle   import *
from time      import sleep

cs(autoreset=True) # sys.base_prefix('  ')

api_url     = "https://lookup.binlist.net"
api_headers = {'Accept-Version': '3'}

#                          nuir c.


class ui:

    def message(msg):
        """
        msg: str/message message like: x,x,x ...
        """
        
        print(f'[ {c.LIGHTYELLOW_EX}›{c.RESET} | {c.BLUE}nuir-c{c.RESET} ] ⟬ {msg} ⟭')
        
    def success(msg):
        """
        msg: str/success message like: correct!, yeah!, cloped ...
        """
        
        print(f'[ {c.LIGHTGREEN_EX}!{c.RESET} | {c.BLUE}nuir-c{c.RESET} ] ⟬ {msg} ⟭')
        
    def unkown():
        """
        unkown message: unkown error
        no args ❌
        """
        
        print(f'[ {c.YELLOW}?{c.RESET} {c.BLUE}nuir-c{c.RESET} ] ⟬ unkown error ⟭')
        
    def error(msg):
        """
        msg: str/error message like: ups..., incorrect word, try again ...
        """
        
        print(f'[ {c.RED}-{c.RESET} | {c.BLUE}nuir-c{c.RESET} ] ⟬ {msg} ⟭')
        
    def clear():
        """
        only clear the screen
        no args ❌
        """

        os.system('cls')

class api:
    def start(b="5416125253517959") -> None:
        
        global info
        """
        b: str/credit card number like: 5416125253517959
        """
        
        ui.clear()
        ui.success('starting!')
        sleep(2.994)
        ui.clear()
        
        if b == "5416125253517959":

            b = b[0:6]
            r = get(f'{api_url}/{b}',headers=api_headers)
            
            info = r.json() # r.text (...)
            brand   = info.get('scheme')
            type    = info.get('type')
            bank    =  info.get('bank', {}).get('name')
            country = info.get('country', {}).get('name')
            
            rsl = f"""
            {c.LIGHTRED_EX}╔══════════════════════════════╗ ╔═════════════════════════╗{c.RESET}                
            {c.LIGHTRED_EX}║{c.RESET}{c.BLUE}   _  _ _  _ _ ____    ____ {c.RESET}  {c.LIGHTRED_EX}║ {c.RESET}{c.LIGHTRED_EX}║{c.RESET} {c.LIGHTRED_EX}›{c.LIGHTWHITE_EX}pypi.org/project/nuirc{c.LIGHTYELLOW_EX}¹{c.RESET}{c.LIGHTRED_EX}║{c.RESET}
            {c.LIGHTRED_EX}║{c.RESET}{c.BLUE}   |\ | |  | | |__/ __ |    {c.RESET}  {c.LIGHTRED_EX}║{c.RESET} {c.LIGHTRED_EX}║{c.RESET} {c.LIGHTRED_EX}›{c.LIGHTWHITE_EX}github.com/xlitus{c.LIGHTYELLOW_EX}₂{c.RESET}     {c.LIGHTRED_EX}║{c.RESET}
            {c.LIGHTRED_EX}║{c.RESET}{c.BLUE}   | \| |__| | |  \    |___ .{c.RESET} {c.LIGHTRED_EX}║{c.RESET} {c.LIGHTRED_EX}║{c.RESET} {c.LIGHTRED_EX}›{c.LIGHTWHITE_EX}by xlitus{c.RESET}              {c.LIGHTRED_EX}║{c.RESET}
            {c.LIGHTRED_EX}║{c.RESET}{c.BLUE}                             {c.RESET} {c.LIGHTRED_EX}║{c.RESET} {c.LIGHTRED_EX}║{c.RESET}         {c.LIGHTRED_EX}⟦ {c.BLUE}NUIR C.{c.LIGHTRED_EX} ⟧{c.RESET}     {c.LIGHTRED_EX}║{c.RESET}
            {c.LIGHTRED_EX}╚══════════════════════════════╝ ╚═════════════════════════╝{c.RESET}                           

                    {c.LIGHTRED_EX}› {c.BLUE}{b}
                    {c.LIGHTRED_EX}- {c.BLUE}{brand}
                    {c.LIGHTRED_EX}- {c.BLUE}{type}
                    {c.LIGHTRED_EX}- {c.BLUE}{country}
                    {c.LIGHTRED_EX}- {c.BLUE}{bank}
            {c.RESET}
            """
            print(rsl)

            ui.message('you need put a credit card/bin. this cc is only a example')
            
        else:
            b = b[0:6]
            r = get(f'{api_url}/{b}',headers=api_headers)
            
            info = r.json() # r.text x.
            
            brand   = info.get('scheme')
            type    = info.get('type')
            bank    =  info.get('bank', {}).get('name')
            country = info.get('country', {}).get('name')
            
            rsl = f"""
            {c.LIGHTRED_EX}╔══════════════════════════════╗ ╔═════════════════════════╗{c.RESET}                
            {c.LIGHTRED_EX}║{c.RESET}{c.BLUE}   _  _ _  _ _ ____    ____ {c.RESET}  {c.LIGHTRED_EX}║ {c.RESET}{c.LIGHTRED_EX}║{c.RESET} {c.LIGHTRED_EX}›{c.LIGHTWHITE_EX}pypi.org/project/nuirc{c.LIGHTYELLOW_EX}¹{c.RESET}{c.LIGHTRED_EX}║{c.RESET}
            {c.LIGHTRED_EX}║{c.RESET}{c.BLUE}   |\ | |  | | |__/ __ |    {c.RESET}  {c.LIGHTRED_EX}║{c.RESET} {c.LIGHTRED_EX}║{c.RESET} {c.LIGHTRED_EX}›{c.LIGHTWHITE_EX}github.com/xlitus{c.LIGHTYELLOW_EX}₂{c.RESET}     {c.LIGHTRED_EX}║{c.RESET}
            {c.LIGHTRED_EX}║{c.RESET}{c.BLUE}   | \| |__| | |  \    |___ .{c.RESET} {c.LIGHTRED_EX}║{c.RESET} {c.LIGHTRED_EX}║{c.RESET} {c.LIGHTRED_EX}›{c.LIGHTWHITE_EX}by xlitus{c.RESET}              {c.LIGHTRED_EX}║{c.RESET}
            {c.LIGHTRED_EX}║{c.RESET}{c.BLUE}                             {c.RESET} {c.LIGHTRED_EX}║{c.RESET} {c.LIGHTRED_EX}║{c.RESET}         {c.LIGHTRED_EX}⟦ {c.BLUE}NUIR C.{c.LIGHTRED_EX} ⟧{c.RESET}     {c.LIGHTRED_EX}║{c.RESET}
            {c.LIGHTRED_EX}╚══════════════════════════════╝ ╚═════════════════════════╝{c.RESET}                           

                    {c.LIGHTRED_EX}› {c.BLUE}{b}
                    {c.LIGHTRED_EX}- {c.BLUE}{brand}
                    {c.LIGHTRED_EX}- {c.BLUE}{type}
                    {c.LIGHTRED_EX}- {c.BLUE}{country}
                    {c.LIGHTRED_EX}- {c.BLUE}{bank}
            {c.RESET}
            """
            print(rsl)
            ui.message('check nuir-c. github for check new version/s')
