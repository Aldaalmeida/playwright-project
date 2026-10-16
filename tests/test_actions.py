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
    

    # comando press_sequentially (digita o texto letra por letra, simulando a digitação real de um usuário.) Delay deixa a digitação mais lenta

    page.get_by_role("textbox", name="Username: (admin)").press_sequentially("admin", delay=500)
    page.get_by_role("textbox", name="Password: (1234)").press_sequentially("1234", delay=500)
    page.get_by_role("textbox", name="Select a date:").press_sequentially("12/05/2026", delay=500)
  

    # Ações para clicar em checkboxes e raddio Buttons

    # check

    time.sleep(6)
    page.get_by_role("checkbox", name="Feature 1").check()
    page.get_by_role("checkbox", name="Feature 2").check()
    page.get_by_role("radio", name="Option B").check()

    # Para confirmar se aquela opção realmente está marcada podemos usar o to_be_checked

    expect(page.get_by_role("radio", name="Option B")).to_be_checked()
    time.sleep(6)

    #Select_option

    page.get_by_label("Choose an option:").select_option("Option 2")
    time.sleep(6)

    # Click Actions, mouse action

    #.clike - (é utilizado para botões de clique simples, apenas um clique)

    page.get_by_role("button", name="Single Click").click()
    expect(page.get_by_text("Single click button clicked")).to_be_visible()
    time.sleep(5)

    #.dblclick - ( é utilizado para botões de clique duplo, dois  cliques)

    page.get_by_role("button", name="Double Click").dblclick()
    expect(page.get_by_text("Double click button clicked")).to_be_visible()
    time.sleep(5)

    # Right click - ( Clique com o botão direito, para esse usamos: .click(button="right")
    
    page.get_by_role("button", name="Right Click").click(button="right")
    expect(page.get_by_text("Right click button clicked")).to_be_visible
    time.sleep(5)

    # Shift + Clik - ( Simula uma tecla pressionada junto com o clique)

    page.get_by_role("button", name="Shift + Click").click(modifiers=["Shift"])
    expect(page.get_by_text("Please use Shift + Click!")).to_be_visible
    time.sleep(5)

    # Hover Menu - (Passar o Mouse - Move o cursor sobre um elemento sem clicar, para esse usamos: . hover
     
    page.get_by_text("Hover Menu").hover()
    page.get_by_role("link", name="Option 1").click()
    expect(page).to_have_url("https://leogcarvalho.github.io/test-automation-practice/#option1")
    time.sleep(5)

    # Keyboard Actions - Comandos usando teclas do teclado

    # Usando o .press(" Aqui o nome da tecla")

    page.get_by_role("textbox", name="Username: (admin)").fill("admin")
    page.get_by_role("textbox", name="Username: (admin)").press("Tab")
    page.get_by_role("textbox", name="Password: (1234)").fill("1234")
    page.get_by_role("textbox", name="Password: (1234)").press("Enter")
    time.sleep(5)

    # Fazendo Upload de Arquivos com o Playwright

    # .set_input_files

    page.get_by_role("button", name="Choose File").set_input_files("files/Simple.txt")
    time.sleep(5)

    # #Também é possivel limpar os arquivos enviados usando o .set_input_files([])

    page.get_by_role("button", name="Choose File").set_input_files([])

    # Drag and Drop - (O comando drag_to() é utilizado para simular a ação de arrastar e soltar um elemento em outro local da tela.)

    page.get_by_text("Drag me").drag_to(page.get_by_text("Drop here"))
    expect(page.get_by_text("Item successfully dropped!")).to_be_visible
    time.sleep(6)