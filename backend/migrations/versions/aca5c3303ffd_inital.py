"""inital

Revision ID: aca5c3303ffd
Revises: 
Create Date: 2024-07-12 22:14:25.013031

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'aca5c3303ffd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist_profiles',
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_available', sa.Boolean(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producer_profiles',
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_available', sa.Boolean(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_available', sa.Boolean(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_available', sa.Boolean(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('artist_tags_association',
    sa.Column('artist_profile_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_profile_id'], ['artist_profiles.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], )
    )
    op.create_table('producer_tags_association',
    sa.Column('producer_profile_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['producer_profile_id'], ['producer_profiles.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], )
    )
    op.create_table('users',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('picture_url', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=False),
    sa.Column('registered_at', sa.DateTime(), nullable=False),
    sa.Column('artist_profile_id', sa.Integer(), nullable=True),
    sa.Column('producer_profile_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_available', sa.Boolean(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['artist_profile_id'], ['artist_profiles.id'], ),
    sa.ForeignKeyConstraint(['producer_profile_id'], ['producer_profiles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('albums',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('picture_url', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('co_prod', sa.String(), nullable=True),
    sa.Column('prod_by', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_available', sa.Boolean(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('listener_tags_association',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('squads',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('picture', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('file_path', sa.String(), nullable=False),
    sa.Column('co_prod', sa.String(), nullable=True),
    sa.Column('prod_by', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_available', sa.Boolean(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tracks',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('picture_url', sa.String(), nullable=True),
    sa.Column('file_url', sa.String(), nullable=False),
    sa.Column('co_prod', sa.String(), nullable=True),
    sa.Column('prod_by', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_available', sa.Boolean(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_to_roles_association',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'role_id')
    )
    op.create_table('album_track_association',
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.Column('track_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], )
    )
    op.create_table('artist_profile_album_association',
    sa.Column('artist_profile_id', sa.Integer(), nullable=True),
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['artist_profile_id'], ['artist_profiles.id'], )
    )
    op.create_table('artist_profile_track_association',
    sa.Column('artist_profile_id', sa.Integer(), nullable=True),
    sa.Column('track_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_profile_id'], ['artist_profiles.id'], ),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], )
    )
    op.create_table('squad_artist_profile_association',
    sa.Column('squad_id', sa.Integer(), nullable=True),
    sa.Column('artist_profile_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_profile_id'], ['artist_profiles.id'], ),
    sa.ForeignKeyConstraint(['squad_id'], ['squads.id'], )
    )
    op.create_table('squad_producer_profile_association',
    sa.Column('squad_id', sa.Integer(), nullable=True),
    sa.Column('producer_profile_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['producer_profile_id'], ['producer_profiles.id'], ),
    sa.ForeignKeyConstraint(['squad_id'], ['squads.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('squad_producer_profile_association')
    op.drop_table('squad_artist_profile_association')
    op.drop_table('artist_profile_track_association')
    op.drop_table('artist_profile_album_association')
    op.drop_table('album_track_association')
    op.drop_table('user_to_roles_association')
    op.drop_table('tracks')
    op.drop_table('squads')
    op.drop_table('listener_tags_association')
    op.drop_table('albums')
    op.drop_table('users')
    op.drop_table('producer_tags_association')
    op.drop_table('artist_tags_association')
    op.drop_table('tags')
    op.drop_table('roles')
    op.drop_table('producer_profiles')
    op.drop_table('artist_profiles')
    # ### end Alembic commands ###
