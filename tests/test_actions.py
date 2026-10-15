from playwright.sync_api import Page, expect
import time

def test_actions(page: Page) -> None:
    page.goto("https://leogcarvalho.github.io/test-automation-practice/")

    # Comandos para preencher campos

    # Comando Fill (preenche os campos tudo de uma vez.)

    page.get_by_role("textbox", name="Username: (admin)").click()
    page.get_by_role("textbox", name="Username: (admin)").fill("admin")
    page.get_by_role("textbox", name="Username: (admin)").press("Enter")
    page.get_by_role("textbox", name="Password: (1234)").fill("1234")
    

    #comando press_sequentially (digita o texto letra por letra, simulando a digitação real de um usuário.) Delay deixa a digitação mais lenta

    page.get_by_role("textbox", name="Username: (admin)").press_sequentially("admin", delay=500)
    page.get_by_role("textbox", name="Password: (1234)").press_sequentially("1234", delay=500)
    page.get_by_role("textbox", name="Select a date:").press_sequentially("12/05/2026", delay=500)
  

    # Ações para clicar em checkboxes e raddio Buttons

    #check

    time.sleep(6)
    page.get_by_role("checkbox", name="Feature 1").check()
    page.get_by_role("checkbox", name="Feature 2").check()
    page.get_by_role("radio", name="Option B").check()

    #Para confirmar se aquela opção realmente está marcada podemos usar o to_be_checked
    expect(page.get_by_role("radio", name="Option B")).to_be_checked()
    time.sleep(6)

    #Select_option

    page.get_by_label("Choose an option:").select_option("Option 2")
    time.sleep(6)

    # Ações de cliques, mouse action

