import pytest


from task1.app import check_document_existance, documents, get_doc_owner_name, get_all_doc_owners_names, \
    remove_doc_from_shelf, directories, add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, \
    show_document_info, show_all_docs_info

docs = (doc['number'] for doc in documents)

doc_owners = set(doc['name'] for doc in documents)


class Test:

    @pytest.mark.parametrize("doc", docs)
    def test_check_document_existance(self, doc):
        assert check_document_existance(doc) is True

    def test_get_doc_owner_name(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "11-2")
        assert get_doc_owner_name() == "Геннадий Покемонов"

    def test_get_all_doc_owners_names(self):
        assert get_all_doc_owners_names() == doc_owners

    def test_remove_doc_from_shelf(self):
        doc_number = '11-2'
        remove_doc_from_shelf(doc_number)
        assert doc_number not in directories

    def test_add_new_shelf(self):
        new_shelf_number = '25'
        add_new_shelf(shelf_number=new_shelf_number)
        assert new_shelf_number in directories.keys()

    def test_append_doc_to_shelf(self):
        new_doc_number = '777'
        shelf_number = '1'
        append_doc_to_shelf(shelf_number=shelf_number, doc_number=new_doc_number)
        assert new_doc_number in directories[shelf_number]

    def test_delete_doc(self, monkeypatch):
        del_doc_number = '11-2'
        monkeypatch.setattr("builtins.input", lambda _: del_doc_number)
        delete_doc()
        doc_numbers = set()
        for i in documents:
            doc_numbers.add(i['number'])
        assert del_doc_number not in doc_numbers

    def test_get_doc_shelf(self, monkeypatch):
        doc_number = '11-2'
        monkeypatch.setattr("builtins.input", lambda _: doc_number)
        assert get_doc_shelf() is None

    def test_show_document_info(self):
        assert show_document_info(documents[0]) == print('passport "2207 876234" "Василий Гупкин"')

    def test_show_all_docs_info(self):
        assert show_all_docs_info() == print('Список всех документов:\n')

    def test_move_doc_to_shelf(self, monkeypatch):
        doc_number = '11-2'
        doc_number_and_shelf_number = iter([doc_number, '2'])
        monkeypatch.setattr('builtins.input', lambda _: next(doc_number_and_shelf_number))
        move_doc_to_shelf()
        assert doc_number not in directories['1'] and doc_number in directories['2']
