from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


driver.get('https://twitter.com/login')

try:
    while True:
        input("Haz clic en un elemento y luego presiona Enter...")
        element = driver.switch_to.active_element
        tag_name = element.tag_name
        element_id = element.get_attribute('id')
        element_class = element.get_attribute('class')
        element_xpath = driver.execute_script("function absoluteXPath(element) { var comp, comps = []; var parent = null; var xpath = ''; var getPos = function(element) { var position = 1, curNode; if (element.nodeType == Node.ATTRIBUTE_NODE) { return null; } for (curNode = element.previousSibling; curNode; curNode = curNode.previousSibling) { if (curNode.nodeName == element.nodeName) { ++position; } } return position; }; if (element instanceof Document) { return '/'; } for (; element && !(element instanceof Document); element = element.nodeType == Node.ATTRIBUTE_NODE ? element.ownerElement : element.parentNode) { comp = comps[comps.length] = {}; switch (element.nodeType) { case Node.TEXT_NODE: comp.name = 'text()'; break; case Node.ATTRIBUTE_NODE: comp.name = '@' + element.nodeName; break; case Node.PROCESSING_INSTRUCTION_NODE: comp.name = 'processing-instruction()'; break; case Node.COMMENT_NODE: comp.name = 'comment()'; break; case Node.ELEMENT_NODE: comp.name = element.nodeName; break; } comp.position = getPos(element); } for (var i = comps.length - 1; i >= 0; i--) { comp = comps[i]; xpath += '/' + comp.name.toLowerCase(); if (comp.position !== null) { xpath += '[' + comp.position + ']'; } } return xpath; }; return absoluteXPath(arguments[0]);", element)
        element_test_id = element.get_attribute('data-testid')

        print("Elemento clicado - Tag:", tag_name)
        print("ID:", element_id)
        print("Clases:", element_class)
        print("XPath:", element_xpath)
        print("Test-ID:", element_test_id)

except KeyboardInterrupt:
    print("Programa finalizado por el usuario.")
finally:
    driver.quit()