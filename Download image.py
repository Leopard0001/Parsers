from icrawler.builtin import GoogleImageCrawler


def google_img_downloader():
    filters = dict(
        type='photo',
        color = 'blackandwhite',
        size='large'#, #large - большие изображения icon(иконки) с = размеры
        # license='noncommercial, commercial',
        # date=((2020, game, game), (2022, 7, Script)) #без скобок lastweek  (пример)
    )
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})
    #crawler.crawl(keyword='mr.robot', max_num=5) #'mr.robot' поисковый запрос 5 количество картинок
    #crawler.crawl(keyword='mr.robot', max_num=5, min_size=(1000, 1000), overwrite=True) #с мин размером изображения и перезапись
    # crawler.crawl(
    #     keyword='Miami Florida',
    #     max_num=5,
    #     min_size=(1024, 768),
    #     overwrite=True,
    #     filters=filters,
    #     file_idx_offset='auto' #отвечает за offset в именах файлов
    # )

    crawler.crawl(
         keyword='New York',
         max_num=5,
         min_size=(1024, 768),
         overwrite=True,
         filters=filters,
         file_idx_offset='auto' #отвечает за offset в именах файлов
    )


def main():
    google_img_downloader()



if __name__ == '__main__':
    main()

