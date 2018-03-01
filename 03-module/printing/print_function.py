def printing_model(unprinting_design , complete_model):
    '''交换两个列表的元素'''
    while unprinting_design:
        word_changing = unprinting_design.pop()
        print('change the WORD : ' + word_changing)
        complete_model.append(word_changing)
    print('NOW THE LIST IS : ')
    for word in complete_model:
        print(word)
