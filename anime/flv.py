"""
Creating an app to watch
anime series
"""
from animeflv import AnimeFLV

with AnimeFLV() as api:
    query = input("Escribe la serie que deseas buscar: ")
    elements = api.search(query)

    if not elements:
        print("No se encontraron series con ese nombre.")
        exit()

    for i, element in enumerate(elements):
        print(f"{i}. {element.title}")

    try:
        selection = int(input("Select option: "))
        
        # Verificar que la selección esté dentro del rango
        if selection < 0 or selection >= len(elements):
            print("Opción no válida.")
            exit()

        selected_element = elements[selection]
        info = api.get_anime_info(selected_element.id)
        info.episodes.reverse()
        
        for j, episode in enumerate(info.episodes):
            print(f"{j} | Episode - {episode.id}")

        index_episode = int(input("Select episode: "))
        
        # Verificar que el episodio esté dentro del rango
        if index_episode < 0 or index_episode >= len(info.episodes):
            print("Episodio no válido.")
            exit()

        episode_id = info.episodes[index_episode].id
        results = api.get_links(selected_element.id, episode_id)

        if not results:
            print("No links found for the selected episode.")
        else:
            for result in results:
                print(f"{result.server} - {result.url}")  # Ajustar según la inspección

    except ValueError as ve:
        print(f"Entrada inválida: {ve}")
    except IndexError as ie:
        print(f"Índice fuera de rango: {ie}")
    except Exception as e:
        print(f"Error inesperado: {e}")
